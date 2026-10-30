#!/usr/bin/env python3
"""Small tmux runner for fixed Codex tasks; ownership is coordination, not isolation."""
import argparse
import json
import os
from pathlib import Path
import re
import shlex
import shutil
import signal
import subprocess
import sys
import time
import uuid

TERMINAL = {'ready_for_review', 'failed', 'stopped'}


def emit(value):
    print(json.dumps(value, ensure_ascii=False))


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def save(path, value, exclusive=False):
    path = Path(path)
    content = json.dumps(value, ensure_ascii=False, indent=2) + '\n'
    if exclusive:
        with path.open('x', encoding='utf-8') as stream:
            stream.write(content)
    else:
        temp = path.with_name(path.name + '.' + uuid.uuid4().hex + '.tmp')
        temp.write_text(content, encoding='utf-8')
        temp.replace(path)


def command(args, check=True):
    result = subprocess.run(args, text=True, capture_output=True, timeout=15)
    if check and result.returncode:
        raise ValueError(f'{args[0]} failed: {result.stderr.strip()}')
    return result


def preflight():
    tmux, codex = shutil.which('tmux'), shutil.which('codex')
    if not tmux or not codex:
        raise ValueError('tmux and codex must already be installed and on PATH')
    version = command([tmux, '-V']).stdout.strip()
    codex_version = command([codex, '--version']).stdout.strip()
    help_text = command([codex, 'exec', '--help']).stdout
    for option in ('--json', '--output-last-message', '-C'):
        if option not in help_text:
            raise ValueError(f'Installed codex exec does not advertise {option}')
    return {'tmux': str(Path(tmux).resolve()), 'codex': str(Path(codex).resolve()),
            'tmux_version': version, 'codex_version': codex_version, 'authentication': 'not checked; no model call made'}


def ownership_key(path, case_cache):
    """Compare future names using their parent filesystem without creating probes."""
    if sys.platform != 'darwin':
        return path.parts
    parent = Path(path.anchor)
    parts = [path.anchor]
    for name in path.parts[1:]:
        existing = parent
        while not existing.exists():
            existing = existing.parent
        if existing not in case_cache:
            # Darwin sys/unistd.h: _PC_CASE_SENSITIVE = 11. Python does not
            # expose its symbolic name in os.pathconf_names on macOS.
            sensitive = os.pathconf(existing, 11)
            if sensitive not in (0, 1):
                raise ValueError(f'Cannot determine filesystem case sensitivity: {existing}')
            case_cache[existing] = bool(sensitive)
        parts.append(name if case_cache[existing] else name.casefold())
        parent /= name
    return tuple(parts)


def ownership_overlaps(left, right):
    length = min(len(left), len(right))
    return left[:length] == right[:length]


def validate_plan(project, plan):
    if not isinstance(plan, dict) or not isinstance(plan.get('context'), str) or not plan['context'].strip():
        raise ValueError('Plan requires nonempty context')
    tasks = plan.get('tasks')
    if not isinstance(tasks, list) or not 1 <= len(tasks) <= 8:
        raise ValueError('Plan requires 1..8 tasks')
    ids, paths, case_cache = set(), [], {}
    state_key = ownership_key(project / ".team-standalone", case_cache)
    for task in tasks:
        if not isinstance(task, dict):
            raise ValueError('Each task must be an object')
        tid = task.get('id')
        if not isinstance(tid, str) or not re.fullmatch(r'[a-zA-Z0-9][a-zA-Z0-9_-]{0,47}', tid) or tid.casefold() in ids or tid.upper() in {'GO', 'STOP'}:
            raise ValueError('Task IDs must be unique safe names (letters, digits, underscore, dash); GO and STOP are reserved')
        ids.add(tid.casefold())
        for key in ('role', 'instructions'):
            if not isinstance(task.get(key), str) or not task[key].strip():
                raise ValueError(f'{tid} requires nonempty {key}')
        owned = task.get('write_paths')
        if not isinstance(owned, list):
            raise ValueError(f'{tid} requires write_paths (empty means read-only)')
        for raw in owned:
            if not isinstance(raw, str) or not raw or raw in ('.', './'):
                raise ValueError('write_paths must contain nonempty project-relative paths')
            path = Path(raw)
            if path.is_absolute() or '..' in path.parts or raw.startswith('~'):
                raise ValueError(f'Unsafe write path: {raw}')
            resolved = (project / path).resolve()
            if resolved == project or project not in resolved.parents:
                raise ValueError(f'Write path escapes project: {raw}')
            key = ownership_key(resolved, case_cache)
            if key[:len(state_key)] == state_key:
                raise ValueError('Workers may not own runner state')
            for other_id, other in paths:
                if other_id != tid and ownership_overlaps(key, other):
                    raise ValueError(f'Overlapping write_paths: {tid} and {other_id}')
            paths.append((tid, key))
    return plan


def load_run(raw):
    path = Path(raw)
    if not path.is_absolute():
        raise ValueError('--run must be absolute')
    if path.is_symlink() or any(parent.is_symlink() for parent in path.parents):
        raise ValueError('Run path must not contain symlinks')
    path = path.resolve()
    if path.parent.name != '.team-standalone' or not re.fullmatch(r'[a-f0-9]{32}', path.name):
        raise ValueError('Invalid run directory identity')
    for entry in path.rglob('*'):
        if entry.is_symlink():
            raise ValueError('Run artifacts must not contain symlinks')
    data = read(path / 'run.json')
    if data['run'] != str(path) or not re.fullmatch(r'fde-team-[a-f0-9]{16}', data['socket']):
        raise ValueError('Run identity mismatch')
    if data['session'] != 'team' or data['run_id'] != path.name:
        raise ValueError('Run identity mismatch')
    if Path(data['project']).resolve() != path.parent.parent:
        raise ValueError('Run project identity mismatch')
    validate_plan(Path(data['project']), read(path / 'plan.json'))
    if data['tasks'] != read(path / 'plan.json')['tasks']:
        raise ValueError('Run tasks do not match immutable input plan')
    return path, data


def tmux(data, *args, check=True):
    return command([data['tmux'], '-L', data['socket'], *args], check=check)


def session_exists(data):
    result = tmux(data, 'has-session', '-t', '=' + data['session'], check=False)
    if result.returncode == 0:
        return True
    diagnostic = result.stderr.strip()
    socket_path = r'[^\n]+/' + re.escape(data['socket'])
    known_absent = (
        diagnostic == "can't find session: " + data['session']
        or re.fullmatch(r'error connecting to ' + socket_path + r' \(No such file or directory\)', diagnostic)
        or re.fullmatch(r'no server running on ' + socket_path, diagnostic)
    )
    if result.returncode == 1 and known_absent:
        return False
    raise ValueError('Cannot determine whether the exact tmux session exists: ' +
                     (diagnostic or f'exit {result.returncode} without a diagnostic'))


def verify_session(data):
    result = tmux(data, 'show-options', '-qv', '-t', '=' + data['session'] + ':', '@fde_run', check=False)
    if result.returncode or result.stdout.strip() != data['run_id']:
        # The last pane may exit between has-session and show-options. An exact
        # missing target is safe to report as absent; a live mismatch is not.
        if not session_exists(data):
            return False
        raise ValueError('tmux session identity does not match this run; refusing operation')
    return True


def panes(data):
    if not session_exists(data) or not verify_session(data):
        return {}
    result = tmux(data, 'list-panes', '-s', '-t', '=' + data['session'] + ':',
                  '-F', '#{pane_id} #{pane_dead}', check=False)
    if result.returncode:
        if not session_exists(data):
            return {}
        raise ValueError('Cannot inspect the exact team session; refusing operation')
    if not verify_session(data):
        return {}
    return {line.split()[0]: line.split()[1] == '1' for line in result.stdout.splitlines()}


def status(path, data):
    current = panes(data)
    output = []
    for task in data['tasks']:
        folder = path / task['id']
        state_path = folder / 'process.json'
        state = read(state_path) if state_path.exists() else {'state': 'planned'}
        launch = read(folder / 'launch.json') if (folder / 'launch.json').exists() else {}
        pane = launch.get('pane')
        dead = current.get(pane)
        if launch.get('never_launched') is True and not state_path.exists():
            state = {'state': 'stopped', 'group_stopped': True,
                     'evidence': 'Start aborted before invoking this task tmux spawn command'}
        process_state = state['state']
        proven = process_state in TERMINAL and state.get('group_stopped') is True
        if not proven and dead is not False:
            process_state = 'interrupted_or_unknown'
        output.append({'id': task['id'], 'pane': pane, 'pane_dead': dead,
                       'process_state': process_state, 'stopped': proven and dead is not False,
                       'review': read(folder / 'review.json') if (folder / 'review.json').exists() else None,
                       'process': state, 'result': str(folder / 'result.md'),
                       'log': str(folder / 'output.jsonl')})
    return {'run': str(path), 'socket': data['socket'], 'session': data['session'],
            'stop_requested': (path / 'STOP').exists(), 'tasks': output}


def start(args):
    project = Path(args.project)
    if not project.is_absolute() or not project.is_dir():
        raise ValueError('--project must be an existing absolute directory')
    project = project.resolve()
    plan = validate_plan(project, read(args.plan))
    env = preflight()
    base = project / '.team-standalone'
    if base.is_symlink():
        raise ValueError('Runner state directory must not be a symlink')
    base.mkdir(exist_ok=True)
    run_id = uuid.uuid4().hex
    path = base / run_id
    path.mkdir()
    data = dict(env, run=str(path), run_id=run_id, project=str(project),
                socket='fde-team-' + run_id[:16], session='team', tasks=plan['tasks'])
    save(path / 'run.json', data, exclusive=True)
    save(path / 'plan.json', plan, exclusive=True)
    for task in plan['tasks']:
        folder = path / task['id']
        folder.mkdir()
        save(folder / 'task.json', task, exclusive=True)
        prompt = ('You are one worker in a shared project. Other workers are active: do not revert their edits.\n'
                  'Perform only this fixed task; do not start nested teams, spawn agents, or modify Codex settings/auth/models/hooks.\n'
                  'Read applicable AGENTS.md. Write only assigned paths; empty write_paths means read-only. '
                  'Shared coordination files (AGENTS.md, HANDOFF.md, docs/STATE.md) belong to the leader; do not edit them. '
                  'Do not edit .team-standalone state. Do not commit or push. Stop any tests/services you start before finishing. '
                  'Report any scope conflict instead of expanding scope.\n'
                  'Your final message must include: Goal understanding, Outcome, Changed files, Verification commands and results, '
                  'Blockers/uncertainties. Do not claim tests ran unless they did.\n\nContext:\n' + plan['context'] +
                  '\n\nAssignment:\n' + json.dumps(task, ensure_ascii=False, indent=2))
        (folder / 'prompt.txt').write_text(prompt, encoding='utf-8')
    attempted = set()
    try:
        for index, task in enumerate(plan['tasks']):
            shell_command = 'exec ' + shlex.join([sys.executable, str(Path(__file__).resolve()),
                                                  '_worker', '--run', str(path), '--task', task['id']])
            # Record intent before invocation: a timed-out spawn is ambiguous, never 'not launched'.
            attempted.add(task['id'])
            if index == 0:
                result = tmux(data, 'new-session', '-d', '-s', 'team', '-n', task['id'],
                              '-P', '-F', '#{pane_id}', shell_command)
            else:
                result = tmux(data, 'new-window', '-d', '-t', '=team:', '-n', task['id'],
                              '-P', '-F', '#{pane_id}', shell_command)
            save(path / task['id'] / 'launch.json', {'pane': result.stdout.strip()}, exclusive=True)
            if index == 0:
                tmux(data, 'set-option', '-t', '=team:', '@fde_run', run_id)
                tmux(data, 'set-option', '-w', '-g', 'remain-on-exit', 'on')
        (path / 'GO').touch(exist_ok=False)
    except Exception as exc:
        (path / 'STOP').touch()
        for task in plan['tasks']:
            if task['id'] not in attempted:
                save(path / task['id'] / 'launch.json', {'never_launched': True}, exclusive=True)
        raise ValueError(f'Partial start; cancellation requested, artifacts retained at {path}: {exc}') from exc
    return {'run': str(path), 'socket': data['socket'], 'session': data['session'],
            'tasks': [{'id': task['id'], **read(path / task['id'] / 'launch.json')} for task in data['tasks']]}


def group_alive(pid):
    try:
        os.killpg(pid, 0)
        return True
    except ProcessLookupError:
        return False
    except PermissionError:
        return True


def terminate(child):
    for sig, seconds in ((signal.SIGTERM, 3), (signal.SIGKILL, 3)):
        if not group_alive(child.pid):
            break
        try:
            os.killpg(child.pid, sig)
        except ProcessLookupError:
            pass
        deadline = time.monotonic() + seconds
        while time.monotonic() < deadline:
            child.poll()  # Reap the direct child before checking its process group.
            if not group_alive(child.pid):
                break
            time.sleep(.1)
    child.poll()
    return child.returncode is not None and not group_alive(child.pid)


def worker(args):
    path, data = load_run(args.run)
    if args.task not in {task['id'] for task in data['tasks']}:
        raise ValueError('Unknown task')
    folder = path / args.task
    # Exactly one wrapper can ever own this task. No automatic relaunch on failure.
    with (folder / 'wrapper.lock').open('x') as stream:
        stream.write(str(os.getpid()))
    interrupted = [False]
    def on_signal(signum, frame):
        interrupted[0] = True
    for sig in (signal.SIGTERM, signal.SIGHUP, signal.SIGINT):
        signal.signal(sig, on_signal)
    state = {'state': 'starting', 'wrapper_pid': os.getpid(), 'pane': os.environ.get('TMUX_PANE')}
    save(folder / 'process.json', state)
    child = None
    try:
        deadline = time.monotonic() + 60
        while not (path / 'GO').exists():
            if interrupted[0] or (path / 'STOP').exists() or time.monotonic() > deadline:
                state.update(state='stopped', group_stopped=True)
                return
            time.sleep(.1)
        if interrupted[0] or (path / 'STOP').exists():
            state.update(state='stopped', group_stopped=True)
            return
        with (folder / 'prompt.txt').open('rb') as prompt, (folder / 'output.jsonl').open('wb') as output:
            child = subprocess.Popen([data['codex'], 'exec', '-C', data['project'], '--json',
                                      '--output-last-message', str(folder / 'result.md'), '-'],
                                     stdin=prompt, stdout=output, stderr=subprocess.STDOUT,
                                     cwd=data['project'], start_new_session=True)
            state.update(state='running', child_pid=child.pid)
            save(folder / 'process.json', state)
            while child.poll() is None and not interrupted[0] and not (path / 'STOP').exists():
                time.sleep(.1)
            cancelled = interrupted[0] or (path / 'STOP').exists()
            stopped = terminate(child)
            result = folder / 'result.md'
            has_result = result.is_file() and bool(result.read_text(encoding='utf-8').strip())
            state.update(state='stopped' if cancelled else
                         ('ready_for_review' if child.returncode == 0 and has_result and stopped else 'failed'),
                         exit_code=child.returncode, group_stopped=stopped)
    except Exception as exc:
        stopped = terminate(child) if child is not None else True
        state.update(state='failed', error=str(exc), group_stopped=stopped)
    finally:
        save(folder / 'process.json', state)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('preflight')
    launch = sub.add_parser('start')
    launch.add_argument('--project', required=True)
    launch.add_argument('--plan', required=True)
    for name in ('status', 'attach', 'stop', 'shutdown', 'review', '_worker'):
        command_parser = sub.add_parser(name)
        command_parser.add_argument('--run', required=True)
        if name in ('review', '_worker'):
            command_parser.add_argument('--task', required=True)
        if name == 'review':
            command_parser.add_argument('--verdict', choices=['accepted', 'rejected'], required=True)
            command_parser.add_argument('--evidence', required=True)
    args = parser.parse_args()
    if args.command == 'preflight':
        emit(preflight())
        return
    if args.command == 'start':
        emit(start(args))
        return
    if args.command == '_worker':
        worker(args)
        return
    path, data = load_run(args.run)
    if args.command == 'attach':
        if not verify_session(data):
            raise ValueError('The exact team session no longer exists')
        subprocess.run([data['tmux'], '-L', data['socket'], 'attach-session', '-t', '=' + data['session']], check=True)
        return
    if args.command == 'stop':
        (path / 'STOP').touch()
        deadline = time.monotonic() + 10
        while time.monotonic() < deadline:
            report = status(path, data)
            if all(task['stopped'] for task in report['tasks']):
                break
            time.sleep(.2)
        report = status(path, data)
        emit(report)
        if not all(task['stopped'] for task in report['tasks']):
            raise ValueError('Stop incomplete: workers may still be writing or liveness is unknown; artifacts retained')
        return
    report = status(path, data)
    if args.command == 'review':
        task = next((task for task in report['tasks'] if task['id'] == args.task), None)
        if task is None or not task['stopped']:
            raise ValueError('Review requires a known task with proven stopped worker/process group')
        if args.verdict == 'accepted' and task['process_state'] != 'ready_for_review':
            raise ValueError('Only ready_for_review tasks can be accepted')
        if not args.evidence.strip():
            raise ValueError('Review requires nonempty verification evidence')
        record = {'verdict': args.verdict, 'evidence': args.evidence, 'recorded_at': time.time()}
        save(path / args.task / 'review.json', record)
        emit(status(path, data))
    elif args.command == 'shutdown':
        if not all(task['stopped'] for task in report['tasks']):
            raise ValueError('Workers may still be writing or their liveness is unknown; refusing shutdown')
        if not report['stop_requested'] and not all(task['review'] and task['review']['verdict'] == 'accepted' for task in report['tasks']):
            raise ValueError('Shutdown requires all reviews accepted, or explicit stop')
        if session_exists(data) and verify_session(data):
            result = tmux(data, 'kill-session', '-t', '=' + data['session'], check=False)
            if result.returncode and session_exists(data):
                raise ValueError('Could not shut down the exact team session')
        report['shutdown'] = True
        emit(report)
    else:
        emit(report)


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, KeyError, TypeError, subprocess.SubprocessError) as error:
        print(json.dumps({'error': str(error)}, ensure_ascii=False), file=sys.stderr)
        sys.exit(1)
