# 실행 방법과 원본 대비 차이

## 필요한 환경

- macOS 또는 Linux의 Python 3.10 이상, tmux, 이미 사용할 수 있는 Codex CLI.
- 현재 환경의 Codex에서 `exec`, `--json`, `--output-last-message`, `--cd`를 지원해야 한다.
- 시험·조직이 허용한 모델, 인증, 동시 실행, 파일 수정 권한을 그대로 사용한다. tmux 설치만으로 이 조건들이 충족되는 것은 아니다.

실행 파일은 외부 Python 패키지나 OMX를 설치하지 않는다. 별도 CLI는 현재 채팅의 일회성 모델·권한 선택을 그대로 물려받는다고 보장할 수 없다. 이 환경의 CLI 설정이 허용된 것인지 먼저 확인한다. 실행 파일은 설정 파일이나 인증 정보를 출력하지 않는다.

`codex exec`가 읽기 전용으로 실행되는 환경에서는 구현 작업이 막힐 수 있다. 이 스킬은 샌드박스·승인 정책을 덮어쓰지 않는다. 제한을 풀거나 계정·모델을 바꾸는 대신 확인한 제약을 보고한다.

## 1. 명령 위치 확인

아래 세 변수는 실제 절대 경로로 바꾼다. 스킬을 개인 폴더에 등록했다면 `team_helper`도 그 위치를 가리켜야 한다.

```bash
team_helper="/과제/skills/team-standalone/scripts/team.py"
task_root="/실제/과제/폴더"
plan_file="/실제/과제/폴더/team-plan.json"

python3 "$team_helper" preflight
```

`preflight`는 설치 상태와 명령 호환성을 확인한다. AI 요청은 보내지 않으므로 로그인·모델 사용 가능 여부나 실제 수정 권한은 별도 확인 대상이다.

## 2. 작업 계획 저장

아래는 형식 예시다. 파일명·과제·역할은 실제 합의한 작업으로 바꾸고, 계획 파일에는 비밀 키나 인증 정보를 넣지 않는다.

```json
{
  "context": "docs/SPEC.md에 합의한 CSV 검사 기능을 구현한다. 계산 규칙은 SPEC을 따른다. 아래 두 작업은 서로의 변경 결과를 기다리지 않아도 된다.",
  "tasks": [
    {
      "id": "csv-core",
      "role": "CSV 처리 구현",
      "instructions": "docs/SPEC.md를 읽고 src/csv_check.py에 합의한 CSV 검사 함수를 구현한다. 정상 입력과 누락값 입력의 실제 결과를 확인하고 보고한다.",
      "write_paths": ["src/csv_check.py"]
    },
    {
      "id": "input-review",
      "role": "읽기 검토",
      "instructions": "docs/SPEC.md와 제공된 원본 샘플 자료를 읽고 입력 규칙에서 빠진 조건을 검토한다. 파일은 수정하지 않는다. csv-core가 수정하는 구현 파일의 검토는 이번 작업에 포함하지 않는다.",
      "write_paths": []
    }
  ]
}
```

- 한 묶음에 지정한 1~8개 작업을 각각 한 번 실행한다. 보통 2개로 시작하고 실제로 독립적인 일이 있을 때만 늘린다.
- `write_paths`는 프로젝트 기준 상대 파일·폴더 경로다. 빈 배열은 수정할 파일이 없는 작업이다. 절대 경로, 상위 폴더 이동, 전체 프로젝트 지정, 담당 간 겹치는 수정 경로는 거부한다.
- macOS에서는 파일시스템의 대소문자 구분 여부를 확인해 `New.py`와 `new.py`처럼 같은 파일을 가리키는 배정을 거부한다. 구분 여부를 확인하지 못하면 실행을 중단한다. Linux는 일반적인 대소문자 구분 환경을 전제로 하며, 선택적 대소문자 무시 디렉터리와 모든 Unicode 파일명 별칭까지 판별하는 검사는 아니다.
- 이 목록은 협업 범위를 명시하는 장치다. 운영체제의 파일 접근 권한을 새로 제한하는 기능은 아니므로 주 에이전트가 실제 변경도 확인해야 한다.
- 계획에서 한 번 배정한 작업을 실행 중에 바꾸지 않는다. 의존성이 있는 작업은 다음 묶음으로 넘긴다.

## 3. 실행·상태 확인

```bash
python3 "$team_helper" start --project "$task_root" --plan "$plan_file"
```

시작 결과의 `run` 값을 보관한다. 기록은 프로젝트의 `.team-standalone/` 아래 새 실행 폴더에 생긴다. 다른 실행과 겹치지 않는 tmux 연결 이름을 사용하며, 기존 터미널 창을 재사용하거나 닫지 않는다.

```bash
team_run="/실제/과제/폴더/.team-standalone/시작결과의실행폴더"
python3 "$team_helper" status --run "$team_run"
```

창을 직접 보려면 실제 대화형 터미널에서 다음 명령을 사용한다.

```bash
python3 "$team_helper" attach --run "$team_run"
```

`attach`를 지원하지 않는 도구에서는 상태와 저장된 출력으로 확인한다. 재접속을 위해 `start`를 반복하지 않는다.

## 4. 결과 수용과 종료

`ready_for_review`는 Codex 프로세스가 끝나고 최종 응답이 저장됐다는 뜻이다. “권한이 없어 작업하지 못했다”는 응답도 있을 수 있으므로 내용을 읽고 변경·검증 근거를 확인해야 한다.

```bash
python3 "$team_helper" review --run "$team_run" --task csv-core \
  --verdict accepted --evidence "정상 입력과 누락값 입력을 다시 실행했고 SPEC의 기대 결과와 일치함. 실제 실행 명령과 출력은 검증 기록에 저장함."
```

위 evidence는 형식 예시다. 실행하지 않은 검증을 그대로 복사하지 않는다. 검증 실패 시에는 `--verdict rejected`와 실제 이유를 남긴다. 모든 작업 수용 후 필요한 통합 검증까지 끝나면 종료한다.

```bash
python3 "$team_helper" shutdown --run "$team_run"
```

정상 종료는 팀원 프로세스가 모두 멈췄고 작업이 모두 수용됐을 때만 허용한다. 작업 기록·로그·결과는 삭제하지 않는다.

## 5. 실패·중단

```bash
python3 "$team_helper" stop --run "$team_run"
python3 "$team_helper" status --run "$team_run"
python3 "$team_helper" shutdown --run "$team_run"
```

명시적으로 중단한 경우에는 프로세스 종료를 확인한 뒤 수용되지 않은 작업이 있어도 해당 tmux 세션을 닫을 수 있다. 중단은 성공 판정이 아니다. 종료를 증명할 수 없으면 상태를 보존하고 오류를 알린다. 실행 기록을 지우거나 이름이 비슷한 다른 프로세스를 죽여 해결하지 않는다.

종료 확인 범위는 실행기가 시작한 Codex와 같은 프로세스 그룹이다. 팀원이 별도 세션으로 분리한 서버까지 자동으로 찾아 종료하는 기능은 없으므로, 팀원에게 백그라운드 작업을 남기지 않도록 지시하고 남은 작업이 의심되면 주 에이전트가 확인한다. 시작 도중 실패한 경우에도 ‘아직 실행을 시도하지 않은 작업’과 ‘실행 여부가 불명확한 작업’을 구분하며, 후자는 확인 없이 정리하지 않는다.

실패한 작업을 다시 수행할 때는 부분 변경을 먼저 확인한다. 기존 실행이 더 이상 파일을 수정하지 않는 것을 확인한 후, 수정한 작업 지시로 **새 실행**을 만든다. 자동 재시도나 끊긴 AI 대화의 자동 복구는 제공하지 않는다.

## 원본에서 유지한 것과 바꾼 것

| 원본 Team의 역할 | 이 버전 |
| --- | --- |
| 여러 터미널에서 AI 실행 | tmux 창마다 기존 Codex CLI를 한 번 실행 |
| 작업 전 맥락·역할·담당 범위 정리 | 실행 계획과 담당별 지시를 먼저 저장 |
| 작업 상태와 결과 보관 | `.team-standalone/`에 실행별 기록·출력·수용 근거 저장 |
| 주 에이전트의 통합·검증 | 유지. 종료 코드와 완료 판정을 구분 |
| 작업 종료 확인 후 정리 | 유지. 해당 실행의 tmux 세션만 종료, 결과 보존 |
| 팀원 ACK·작업 선점·우편함·재배정 | 고정 배정으로 단순화. 실시간 메시지·자동 재배정 없음 |
| 역할별 모델 선택·Codex/Claude 혼합 | 제거. 기존 Codex CLI 설정만 사용 |
| 자동 worktree 생성·병합 | 제거. 서로 겹치지 않는 파일 담당을 정하는 방식 |
| OMX hooks·HUD·Ultragoal·Ralph 연계 | 제거. OMX 실행·설정 변경 없음 |
| 재개 | 남아 있는 실행을 확인하고 접속. 종료된 AI 작업을 자동 재실행하지 않음 |

원본과의 기능·성능 동등성을 보장하지 않는다. 특히 기록 파일이 있다는 것만으로 원본의 작업 선점·우편함 기능이 생기는 것은 아니다.

## 출처와 확인 범위

- 원본: [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex), 설치 패키지 **0.21.14**의 `skills/team/SKILL.md`, `skills/worker/SKILL.md`, Team 실행 코드 및 운영 규칙을 참고했다. MIT 원문은 상위 폴더의 `LICENSE`에 보존했다.
- 비교한 패키지 원문 SHA-256: Team `f41bbba31e19ffe9c662310eb8d9ae8635052842ecff9122711fc6fa97e9d737`, Worker `aa39e0088c9bbfced4121888cd64ee06f43bbefa2537c9ddbcef5ded35d4b84e`.
- CLI 근거: [Codex 비대화형 실행](https://learn.chatgpt.com/docs/non-interactive-mode), [명령 옵션](https://learn.chatgpt.com/docs/cli/reference). 로컬 `codex-cli 0.164.0`의 도움말도 확인했다.
- 시험 환경에서의 모델 허용·기록 수집·동시 실행·설치 허용 여부는 이 스킬이 보증하지 않는다. 실제 환경에서 확인한 내용만 성공으로 보고한다.
