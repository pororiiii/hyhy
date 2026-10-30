#!/usr/bin/env bash
set -euo pipefail

usage() {
  printf '%s\n' \
    '사용법: bash /키트/절대경로/install.sh --target /실제/과제/폴더' \
    '과제 폴더는 미리 존재해야 합니다. 기존 파일은 덮어쓰지 않습니다.'
}

fail() {
  printf '설치 중단: %s\n' "$1" >&2
  exit 1
}

if [[ $# -eq 1 && ( "$1" == '--help' || "$1" == '-h' ) ]]; then
  usage
  exit 0
fi
if [[ $# -ne 2 || "$1" != '--target' || -z "$2" ]]; then
  usage >&2
  exit 2
fi

kit_root=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)
[[ "$2" == /* ]] || fail '설치 대상은 과제 폴더의 절대 경로로 지정해 주세요.'
[[ -d "$2" ]] || fail '설치 대상 폴더가 없습니다. 실제 과제 폴더를 확인해 주세요.'
task_root=$(cd -- "$2" && pwd -P)
case "$task_root/" in
  "$kit_root/"*) fail '키트 원본 폴더나 그 안에는 설치할 수 없습니다.' ;;
esac

# 현재 선택된 문서와 스킬·부속 파일만 배치합니다.
install_files=(
  AGENTS.md
  HANDOFF.md
  REPOS.md
  docs/STATE.md
  docs/INTERVIEW.md
  docs/AGREEMENT.md
  docs/SPEC.md
  docs/USER_README.md
  skills/handoff/SKILL.md
  skills/deep-interview/SKILL.md
  skills/deep-interview/LICENSE-oh-my-codex
  skills/plan-standalone/SKILL.md
  skills/plan-standalone/LICENSE
  skills/plan-standalone/agents/openai.yaml
  skills/team-standalone/SKILL.md
  skills/team-standalone/LICENSE
  skills/team-standalone/agents/openai.yaml
  skills/team-standalone/references/operations.md
  skills/team-standalone/scripts/team.py
  skills/ultragoal-standalone/SKILL.md
  skills/ultragoal-standalone/LICENSE
  skills/ultragoal-standalone/agents/openai.yaml
  skills/ultragoal-standalone/references/workflow.md
)
install_dirs=(
  docs
  skills
  skills/handoff
  skills/deep-interview
  skills/plan-standalone
  skills/plan-standalone/agents
  skills/team-standalone
  skills/team-standalone/agents
  skills/team-standalone/references
  skills/team-standalone/scripts
  skills/ultragoal-standalone
  skills/ultragoal-standalone/agents
  skills/ultragoal-standalone/references
)

# 복사하기 전에 모든 원본과 대상 경로를 확인합니다.
for relative_dir in "${install_dirs[@]}"; do
  [[ -d "$kit_root/$relative_dir" && ! -L "$kit_root/$relative_dir" ]] || \
    fail "원본이 일반 폴더가 아닙니다: $relative_dir"
done
for relative_path in "${install_files[@]}"; do
  source_path="$kit_root/$relative_path"
  [[ -f "$source_path" && ! -L "$source_path" && -r "$source_path" ]] || \
    fail "필수 원본 파일이 없거나 읽을 수 없습니다: $relative_path"
done

[[ -w "$task_root" ]] || fail '설치 대상 폴더에 쓸 권한이 없습니다.'
for relative_dir in "${install_dirs[@]}"; do
  destination_dir="$task_root/$relative_dir"
  if [[ -L "$destination_dir" || ( -e "$destination_dir" && ! -d "$destination_dir" ) ]]; then
    fail "대상의 $relative_dir 경로가 일반 폴더가 아닙니다. 기존 경로를 보존하고 중단합니다."
  fi
  if [[ -d "$destination_dir" && ( ! -w "$destination_dir" || ! -x "$destination_dir" ) ]]; then
    fail "대상의 $relative_dir 폴더에 쓰거나 접근할 권한이 없습니다."
  fi
done

conflicts=0
for relative_path in "${install_files[@]}"; do
  destination_path="$task_root/$relative_path"
  if [[ -L "$destination_path" ]]; then
    printf '충돌: %s (심볼릭 링크)\n' "$destination_path" >&2
    conflicts=$((conflicts + 1))
  elif [[ -e "$destination_path" ]]; then
    if [[ ! -f "$destination_path" ]] || ! cmp -s "$kit_root/$relative_path" "$destination_path"; then
      printf '충돌: %s (기존 내용 또는 경로 종류가 다름)\n' "$destination_path" >&2
      conflicts=$((conflicts + 1))
    fi
  fi
done
[[ "$conflicts" -eq 0 ]] || fail "사전 검사에서 충돌 ${conflicts}건을 발견했습니다. 파일을 복사하지 않았습니다."

printf '설치 대상: %s\n' "$task_root"
for relative_dir in "${install_dirs[@]}"; do
  destination_dir="$task_root/$relative_dir"
  # 부모를 순서대로 만들고 기존 링크나 파일을 따라가지 않습니다.
  for checked_dir in "${install_dirs[@]}"; do
    [[ ! -L "$task_root/$checked_dir" ]] || fail "설치 중 폴더 경로에 링크가 생겼습니다: $checked_dir"
  done
  if [[ ! -e "$destination_dir" ]]; then
    mkdir -- "$destination_dir" || fail "$relative_dir 폴더를 만들지 못했습니다."
  fi
  [[ -d "$destination_dir" && ! -L "$destination_dir" ]] || fail "설치 중 폴더 경로가 바뀌었습니다: $relative_dir"
done

copied=0
unchanged=0
for relative_path in "${install_files[@]}"; do
  source_path="$kit_root/$relative_path"
  destination_path="$task_root/$relative_path"
  # 사전 검사 뒤 경로가 바뀐 경우에도 다시 확인합니다.
  for relative_dir in "${install_dirs[@]}"; do
    [[ -d "$task_root/$relative_dir" && ! -L "$task_root/$relative_dir" ]] || fail "설치 중 대상 폴더가 바뀌었습니다: $relative_dir"
    [[ -d "$kit_root/$relative_dir" && ! -L "$kit_root/$relative_dir" ]] || fail "설치 중 원본 폴더가 바뀌었습니다: $relative_dir"
  done
  [[ -f "$source_path" && ! -L "$source_path" && -r "$source_path" ]] || fail "설치 중 원본이 바뀌었습니다: $relative_path"
  [[ ! -L "$destination_path" ]] || fail "설치 중 대상에 링크가 생겼습니다: $relative_path"
  if [[ -e "$destination_path" ]]; then
    [[ -f "$destination_path" ]] && cmp -s "$source_path" "$destination_path" || \
      fail "설치 중 대상이 바뀌었습니다: $relative_path. 기존 파일은 보존했습니다."
    unchanged=$((unchanged + 1))
  else
    # noclobber는 검사 직후 같은 경로에 생긴 파일도 덮어쓰지 않게 합니다.
    if ! (set -o noclobber; cat -- "$source_path" > "$destination_path"); then
      fail "파일 쓰기에 실패했습니다: $relative_path. 일부 파일이 배치됐을 수 있으므로 현재 상태를 확인해 주세요."
    fi
    copied=$((copied + 1))
  fi
done

# 성공 여부는 복사 명령의 종료뿐 아니라 실제 위치와 내용으로 확인합니다.
for relative_dir in "${install_dirs[@]}"; do
  [[ -d "$task_root/$relative_dir" && ! -L "$task_root/$relative_dir" ]] || fail "배치 검증 실패: 대상 폴더 $relative_dir"
  [[ -d "$kit_root/$relative_dir" && ! -L "$kit_root/$relative_dir" ]] || fail "배치 검증 실패: 원본 폴더 $relative_dir"
done
for relative_path in "${install_files[@]}"; do
  destination_path="$task_root/$relative_path"
  [[ -f "$destination_path" && ! -L "$destination_path" ]] && \
    cmp -s "$kit_root/$relative_path" "$destination_path" || fail "배치 검증 실패: $relative_path"
done

printf '파일 배치 확인: %s개 (새로 복사 %s개, 같은 내용 유지 %s개)\n' "${#install_files[@]}" "$copied" "$unchanged"
for relative_path in "${install_files[@]}"; do
  printf '확인: %s\n' "$task_root/$relative_path"
done
printf '%s\n' \
  '선택한 문서 양식을 배치했습니다. 실제 과제의 합의·구현 내용은 작업하면서 기록합니다.' \
  'Handoff 스킬 원문은 skills/handoff/SKILL.md에 배치했습니다. AGENTS 안내에 따라 인계 요청 때 참조합니다. AI 도구의 스킬 호출 목록에 등록하는 작업은 별도입니다.' \
  'Deep Interview와 Plan 독립형 스킬 지침·라이선스·메타데이터도 배치했습니다: skills/deep-interview, skills/plan-standalone. AI 도구의 스킬 호출 목록에 등록하는 작업은 별도입니다.' \
  'Team Standalone 스킬과 실행 파일을 skills/team-standalone에 배치했습니다. Python·tmux·Codex CLI가 필요하며 OMX 설치나 Codex 설정 변경은 하지 않았습니다. 실제 팀 실행·스킬 메뉴 등록은 별도입니다.' \
  'Ultragoal Standalone을 skills/ultragoal-standalone에 배치했습니다. tmux·OMX 설치는 필요 없고, Codex Goal 연결은 해당 도구가 제공될 때 선택적으로 사용합니다. 스킬 메뉴 등록은 별도입니다.'
