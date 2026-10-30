# 만들고 싶은 기능별 참고 자료

만들 기능을 아래 목차에서 고르면, 어떤 화면과 동작을 말하는지 설명과 예시를 읽을 수 있다. 그 기능을 만들 AI가 찾아볼 코드 위치도 함께 정리했다.

## 목차

1. **[접수된 점검 요청을 표로 보고 찾기](#category-1)**
   - [1-1. 요청 목록에서 검색·조건 선택·순서 변경하기](#f-ui-list-search-sort-page)
   - [1-2. 요청을 선택해 상세 내용과 처리 기록 보기](#f-ui-record-detail)

2. **[새 점검 요청을 적고 저장·수정·삭제하기](#category-2)**
   - [2-1. 설비명과 고장 내용을 입력해 요청 등록·수정하기](#f-ui-create-edit-validation)
   - [2-2. 저장을 눌렀으면 끝날 때까지 다시 못 누르게 하기](#f-ui-save-inflight)
   - [2-3. 요청을 삭제하기 전에 한 번 더 확인하기](#f-ui-delete-confirm)

3. **[점검 파일을 가져오고 사진을 붙이고 결과를 내려받기](#category-3)**
   - [3-1. CSV 파일에서 설비명과 측정값 읽기](#f-file-csv-read-preview)
   - [3-2. 엑셀 파일을 읽고 검사 결과를 새 엑셀 파일로 만들기](#f-file-xlsx-read-write)
   - [3-3. 점검 요청에 고장 사진을 첨부하고 보관하기](#f-file-attachment-upload)
   - [3-4. 사진을 올리기 전에 잘 골랐는지 확인하기](#f-file-preview-before-save)
   - [3-5. 화면의 검사 결과를 CSV 파일로 내려받기](#f-file-csv-export)

4. **[가져온 검사표에서 빠진 값·중복·잘못된 숫자 찾기](#category-4)**
   - [4-1. 설비명이 없거나 같은 검사번호가 반복된 행 찾기](#f-data-invalid-rows)
   - [4-2. 온도·날짜를 계산할 수 있게 바꾸고 실패한 값 찾기](#f-data-convert)

5. **[점검 값으로 점수·판정·처리 순서 계산하기](#category-5)**
   - [5-1. 긴급도와 영향도를 합쳐 종합 점수 계산하기](#f-rules-weighted-score)
   - [5-2. 측정값을 기준과 비교해 정상·주의·위험으로 나누고 이유 붙이기](#f-rules-condition-reason)
   - [5-3. 점수가 높고 기한이 가까운 요청부터 줄 세우기](#f-rules-priority-sort)

6. **[누가 맡을지 정하고 승인·반려 기록하기](#category-6)**
   - [6-1. 요청 담당자를 정하고 완료 여부 남기기](#f-6-1)
   - [6-2. 내가 검토할 승인 대기 요청만 모아 보기](#f-6-2)
   - [6-3. 요청을 승인하거나 반려하고 누가 했는지 남기기](#f-6-3)

7. **[점검 요청을 세어서 표와 그래프로 보기](#category-7)**
   - [7-1. 전체 요청과 미처리 요청의 건수·비율 계산하기](#f-stats-count-ratio-period)
   - [7-2. 설비를 골라 상세 기록과 그래프 비교하기](#f-dashboard-chart-details)
   - [7-3. 선택한 설비의 평균을 전체 평균과 비교해서 표시하기](#f-dashboard-metric-selection)

8. **[점검 지침을 찾아 답하고 문서 내용을 정리하기](#category-8)**
   - [8-1. 설비 점검 방법을 물으면 관련 지침을 찾아 답하기](#f-ai-document-search)
   - [8-2. AI 답변에서 근거로 쓴 지침 원문 열어 보기](#f-ai-citations)
   - [8-3. 자유롭게 쓴 점검 요청을 설비·증상·담당자 칸으로 나누기](#f-ai-structured-fields)
   - [8-4. 긴 점검 보고서를 나누어 요약한 뒤 모으기](#f-ai-long-summary)
   - [8-5. AI가 읽은 송장 금액을 재계산하고 확인 대기로 두기](#f-ai-review-boundary)

9. **[설비를 점검할 시간을 보고 예약하기](#category-9)**
   - [9-1. 점검 일정을 달력에서 보고 시간 옮기기](#f-9-1)
   - [9-2. 근무시간과 기존 예약을 빼고 점검 가능한 시간 찾기](#f-9-2)
   - [9-3. 점검 예약을 만들고 시간을 바꾸거나 취소하기](#f-9-3)
   - [9-4. 겹치는 점검 시간을 저장하려 하면 경고하기](#f-9-4)

10. **[설비 수치의 이상을 판단할 재료와 알림 처리](#category-10)**
    - [10-1. 최근 온도를 계산해 평소 수준과 비교하기](#f-anomaly-baseline)
    - [10-2. 온도 초과가 계속될 때 이상으로 표시하고 복귀 기록하기](#f-alerts-threshold-state)
    - [10-3. 같은 이상 알림은 줄이고 오래 지속되거나 해결되면 다시 알리기](#f-alerts-dedup-recovery)

11. **[다른 시스템의 점검 요청을 가져오고 반복 처리하기](#category-11)**
    - [11-1. 다른 시스템에서 점검 요청을 가져오거나 처리 결과 보내기](#f-integration-http)
    - [11-2. 정해진 시간 간격으로 새 점검 요청 확인하기](#f-integration-periodic)
    - [11-3. 여러 요청 파일을 나누어 처리하고 결과 모으기](#f-integration-batch)
    - [11-4. 외부 시스템이 잠깐 멈추면 기다렸다 다시 요청하기](#f-integration-retry)

12. **[누가 볼 수 있고 바꿀 수 있는지 정하고 변경 내용 남기기](#category-12)**
    - [12-1. 로그인한 사용자를 확인하고 로그아웃하기](#f-12-1)
    - [12-2. 담당자에게는 자기 요청만, 관리자에게는 전체 요청 보이기](#f-12-2)
    - [12-3. 요청의 수정 전후 내용을 기록하기](#f-12-3)

[AI가 이 자료를 사용할 때 — 사용 원칙·확인 범위](#ai-guide)

## 읽는 법

- **사람이 볼 때:** 시험 전에는 목차와 관심 기능의 예시를 훑어본다. 작업 중에는 AI에게 “합의한 기능에 맞는 REPOS.md 항목을 찾아, 참고할 부분과 직접 만들 부분을 쉬운 말로 설명해줘”라고 요청하면 된다.
- **AI가 기능을 찾을 때:** 먼저 [사용 원칙](#ai-guide)을 확인하고, 목차에서 합의한 기능에 맞는 항목을 고른다. 파일 전체를 먼저 읽기보다 `rg -n 'id="(category-|f-|ai-guide)' REPOS.md`로 위치를 찾고 필요한 항목과 그 분류의 공통 설명을 읽는다. `rg`가 없으면 에디터 검색을 사용한다.
- 각 항목의 예시와 「AI가 참고할 기술 정보」를 함께 보고, 가져올 부분·직접 만들 부분·환경과 한계를 구분한다. 외부 링크를 여는 범위와 접근 실패 시 대처는 아래 [사용 순서](#ai-guide)를 따른다.

## 설명에 사용할 예시

이 문서에서는 가상의 **설비 점검 요청 관리 프로그램**을 예로 든다. 현장 직원이 설비의 이상을 발견해 점검 요청을 등록하고, 담당자가 요청을 찾아 점검·처리하는 프로그램을 생각하면 된다. 실제 해커톤 과제나 구현 범위를 미리 정한 것은 아니다.

본문 예시의 **A-12는 설비에 붙인 이름**, **R-001은 점검 요청 한 건에 붙인 번호**다. 즉, “R-001 요청”은 “A-12 설비에서 진동이 심하니 점검해 달라는 첫 번째 요청”을 가리킨다. 둘 다 설명을 위해 임의로 붙였으며, 목차의 기능을 이해하는 데 알아둘 필요는 없다.

예를 들어 프로그램의 **점검 요청 목록**에는 아래처럼 요청 한 건이 한 줄로 나타난다.

| 요청번호 | 설비명 | 접수 시각 | 처리 상태 | 요청 내용 |
| --- | --- | --- | --- | --- |
| R-001 | A-12 | 10월 29일 09:10 | 미처리 | 작동 중 진동이 심함 |
| R-002 | B-07 | 10월 29일 10:20 | 미처리 | 팬에서 소음이 남 |
| R-003 | A-12 | 10월 29일 11:30 | 완료 | 배관에서 물이 샘 |
| R-004 | A-12 | 10월 29일 11:40 | 미처리 | 온도가 평소보다 높음 |

각 기능의 **예시 상황 → 동작 예시 → 참고 코드가 제공하는 부분 → 따로 만들거나 정할 부분**을 읽으면 된다. 예시의 버튼 이름·화면 문구·숫자는 이해를 돕기 위해 가정한 것으로, 원본 프로그램에 그대로 들어 있다는 뜻은 아니다. 점수 계산·통계 등 다른 항목의 숫자는 해당 항목의 별도 예시다.

**확인 범위:** 참고 코드는 읽었지만 프로그램을 직접 실행하지는 않았다. 실제 과제에 적용한 뒤에는 실행 결과를 확인해야 한다. 파일 경로·함수 이름·연관 파일은 각 항목 아래의 「AI가 참고할 기술 정보」에 있다.

<a id="category-1"></a>

## 1. 접수된 점검 요청을 표로 보고 찾기

목록은 요청번호·설비명·접수일·상태가 나란히 적힌 표를 말한다. 표의 한 행은 점검 요청 한 건이며, 예를 들어 'R-001 / A-12 / 10월 29일 / 미처리'가 한 행이 된다. 여기서 필요한 요청을 찾고 한 행을 눌러 자세한 내용으로 들어가는 화면을 생각하면 된다.

<a id="f-ui-list-search-sort-page"></a>

### 1-1. 요청 목록에서 검색·조건 선택·순서 변경하기

**예시 상황**

예: 담당자가 점검 요청 목록에서 설비 A-12에 관한 미처리 요청만 최신 접수 순으로 보려고 한다.

**동작 예시**

1. 검색창에 'A-12'를 입력한다 → 공통 예시 표에서 설비명이 A-12인 R-001·R-003·R-004만 남는다.
2. 상태에서 '미처리'를 선택한다 → 세 요청 중 완료된 R-003이 빠지고 R-001·R-004만 남는다. 검색어 입력과 별개로 정해진 조건을 고르는 동작이다.
3. 정렬에서 '최신 접수 순'을 선택한다 → 11:40에 접수된 R-004가 09:10에 접수된 R-001보다 위에 온다.
4. 별도로, 같은 조건의 요청이 20건 넘게 쌓인 상황을 생각한다. 첫 20건을 본 뒤 '다음'을 누른다 → 다음 20건을 보여주도록 만든다. 20건은 설명용 설정이다.

**참고 코드가 제공하는 부분**

원본에서 게시물을 검색하고, 조건을 고르고, 정렬하고, 페이지를 옮기는 화면 구성을 참고한다. 설비 점검 요청 화면이 들어 있는 것은 아니므로 게시물 제목·날짜 등의 자리를 우리 설비명·접수일로 바꿔 만든다.

**따로 만들거나 정할 부분**

실제 요청이 저장된 곳에서 검색어·상태·정렬 순서에 맞는 자료와 전체 건수를 가져와 표에 보내는 처리가 필요하다. 화면만 가져오면 R-001 같은 우리 요청이 자동으로 나타나지는 않는다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 검색·조건 필터·정렬·페이지 이동이 있는 목록

- **찾는 말:** 목록 · 검색 · 필터 · 정렬 · 페이지 · pagination · list
- **언제 볼까:** 많은 요청·설비·검사 결과에서 조건에 맞는 행을 찾고 정렬해서 볼 때
- **자료 형태:** 관리 화면 예제·UI 내부 구현 — 서버 연결은 별도
- **저장소·확인 버전:** [marmelab/react-admin](https://github.com/marmelab/react-admin) · [`0c33d9c3c27c`](https://github.com/marmelab/react-admin/commit/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a)

**먼저 볼 코드**

- [examples/simple/src/posts/PostList.tsx](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/examples/simple/src/posts/PostList.tsx) — `postFilter, PostListDesktop, PostListMobile, rowClick`: 검색어 q·제목·불리언 조건을 List에 전달하고 컬럼/기본 정렬·행 클릭·모바일 목록을 연결
- [packages/ra-ui-materialui/src/list/pagination/Pagination.tsx](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/packages/ra-ui-materialui/src/list/pagination/Pagination.tsx) — `Pagination, handlePageChange, handlePerPageChange`: page/perPage/total·이전/다음 가능 여부, 화면의 0 기반 페이지와 데이터의 1 기반 페이지 변환
- [packages/ra-ui-materialui/src/list/ListView.tsx](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/packages/ra-ui-materialui/src/list/ListView.tsx) — `ListView, defaultPagination`: 목록에서 기본 페이지 이동 UI를 붙이고 데이터 없음·로딩 상태를 구분

**참고할 부분과 선정 이유:** 먼저 PostListDesktop의 List → DataTable → DataTable.Col 구성을 읽는다. postFilter를 실제 과제의 검색 항목으로 바꾸고 sort.field와 컬럼 source를 데이터 필드에 맞춘다. page/perPage가 어떻게 연결되는지 필요하면 Pagination을 읽는다. rowClick은 행의 값에 따라 edit 또는 show로 이동하는 분기 예시다.

**함께 볼 파일**

- [examples/simple/src/index.tsx](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/examples/simple/src/index.tsx) — Admin에 데이터 공급자와 Resource를 연결하는 진입점
- [examples/simple/src/posts/index.tsx](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/examples/simple/src/posts/index.tsx) — list/create/edit/show 화면을 posts 자원에 연결
- [examples/simple/src/dataProvider.tsx](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/examples/simple/src/dataProvider.tsx) — 실제 서버가 아닌 fakeRestProvider 기반 예제 데이터 공급자; 실전 API 연결은 별도
- [examples/simple/package.json](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/examples/simple/package.json) — 예제 의존성과 개발·빌드 명령

**환경:** React 18·TypeScript·react-admin 5.15.5 계열·Material UI·react-hook-form. 확인한 examples/simple/package.json 기준이며, 예제는 모노레포 내부 패키지와 fake REST 데이터를 사용한다. 프로젝트의 채택 기술과 다르면 해당 흐름만 참고한다.

**한계·별도로 정할 것:** 검색·정렬·페이지 처리는 dataProvider/API가 같은 규약을 구현해야 한다. UI 파일만 복사하면 작동하지 않는다. PostPanel의 dangerouslySetInnerHTML은 신뢰할 수 없는 문서에 그대로 적용하지 않는다. 서버 성능·실행 결과는 미검증.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: MIT](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/LICENSE.md)

</details>

<a id="f-ui-record-detail"></a>

### 1-2. 요청을 선택해 상세 내용과 처리 기록 보기

**예시 상황**

예: 담당자가 목록에서 R-001을 눌러 A-12의 고장 내용과 이전 처리 기록을 확인하려고 한다.

**동작 예시**

1. 목록에서 R-001 행을 누른다 → R-001 한 건을 보여주는 화면으로 이동한다.
2. '기본 정보'를 누른다 → 설비명 A-12, 요청자, 접수일, 요청 내용을 보여주도록 만든다.
3. '처리 기록'을 누른다 → R-001과 연결된 기록만 모아 보여주도록 만든다.

**참고 코드가 제공하는 부분**

원본은 게시물 한 건의 요약·본문·관련 댓글을 나눠 보여준다. 그 구성을 참고해 점검 요청의 기본 정보와 처리 기록을 서로 다른 칸이나 탭에 배치한다.

**따로 만들거나 정할 부분**

요청 기록과 처리 기록에 같은 요청번호 R-001을 남기고, 상세 화면을 열 때 그 번호에 맞는 자료를 가져오게 해야 한다. 무엇을 처리 기록으로 남길지는 이 예제가 정해주지 않는다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 상세 화면·탭·관련 내역

- **찾는 말:** 상세 · detail · 탭 · 관련 내역 · 첨부 정보
- **언제 볼까:** 선택한 요청이나 장비의 기본 정보와 관련 기록을 한 화면에서 나눠 보여줄 때
- **자료 형태:** 관리 화면 예제·UI 내부 구현 — 서버 연결은 별도
- **저장소·확인 버전:** [marmelab/react-admin](https://github.com/marmelab/react-admin) · [`0c33d9c3c27c`](https://github.com/marmelab/react-admin/commit/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a)

**먼저 볼 코드**

- [examples/simple/src/posts/PostShow.tsx](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/examples/simple/src/posts/PostShow.tsx) — `PostShow, CreateRelatedComment`: useShowController로 한 건을 읽고 TabbedShowLayout으로 요약·본문·관련 댓글을 나눈다

**참고할 부분과 선정 이유:** PostShow의 summary/body/comments 탭을 보고 기본 정보와 관련 기록의 구분 방식을 참고한다. ReferenceManyField의 reference='comments', target='post_id'는 다른 자료에서 현재 항목 ID와 연결되는 행을 읽는 지점이다. 실제 과제의 요청 ID·장비 ID에 맞게 관계를 정해야 한다.

**함께 볼 파일**

- [examples/simple/src/index.tsx](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/examples/simple/src/index.tsx) — Admin에 데이터 공급자와 Resource를 연결하는 진입점
- [examples/simple/src/posts/index.tsx](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/examples/simple/src/posts/index.tsx) — list/create/edit/show 화면을 posts 자원에 연결
- [examples/simple/src/dataProvider.tsx](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/examples/simple/src/dataProvider.tsx) — 실제 서버가 아닌 fakeRestProvider 기반 예제 데이터 공급자; 실전 API 연결은 별도
- [examples/simple/package.json](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/examples/simple/package.json) — 예제 의존성과 개발·빌드 명령
- [examples/simple/src/posts/PostList.tsx](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/examples/simple/src/posts/PostList.tsx) — ShowButton 및 rowClick으로 상세 화면에 진입

**환경:** React 18·TypeScript·react-admin 5.15.5 계열·Material UI·react-hook-form. 확인한 examples/simple/package.json 기준이며, 예제는 모노레포 내부 패키지와 fake REST 데이터를 사용한다. 프로젝트의 채택 기술과 다르면 해당 흐름만 참고한다.

**한계·별도로 정할 것:** 예제의 게시물·댓글 관계를 과제의 관계로 다시 정의해야 한다. RichTextField의 stripTags=false 설정은 외부 HTML을 그대로 표시하는 정책으로 채택하지 않는다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: MIT](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/LICENSE.md)

</details>

<a id="category-2"></a>

## 2. 새 점검 요청을 적고 저장·수정·삭제하기

입력은 '새 점검 요청 등록' 화면의 설비명·고장 내용·우선순위 같은 칸을 채우는 것을 말한다. 로그인창의 입력은 본인이 누구인지 확인하는 목적이고, 검색창의 입력은 이미 있는 자료를 찾는 목적이다. 여기서는 새 업무 기록을 만들거나 이미 저장된 기록을 고치는 입력을 다룬다.

<a id="f-ui-create-edit-validation"></a>

### 2-1. 설비명과 고장 내용을 입력해 요청 등록·수정하기

**예시 상황**

예: 요청자가 등록 화면에 설비명 A-12, 고장 내용 '이상 소음', 우선순위 3을 입력해 새 요청을 만들려고 한다.

**동작 예시**

1. 설비명을 비워 두고 저장을 누른다 → 설비명이 필수라는 안내를 해당 칸 옆에 보여주도록 만든다.
2. 우선순위를 1~3으로 정했다고 가정하고 5를 넣는다 → 허용 범위를 벗어났다고 알려주도록 만든다.
3. 값을 고쳐 저장한다 → 새 요청을 저장한 뒤 결과 화면으로 이동하도록 만든다.
4. 나중에 R-001 수정 화면을 연다 → 기존 내용을 입력칸에 채워 보여주고 변경한 값만 다시 저장하게 한다.

**참고 코드가 제공하는 부분**

원본의 새 게시물 등록·기존 게시물 수정 화면에서 입력칸 배치, 필수값·숫자 범위 검사, 저장 후 이동을 참고한다. 위 설비명과 우선순위 규칙은 설명용이며 원본에 정해진 업무 규칙이 아니다.

**따로 만들거나 정할 부분**

입력받은 설비명·고장 내용·우선순위를 요청 기록에 저장하고, 수정 시 R-001의 기존 값을 불러오는 처리가 필요하다. 잘못된 값을 실제 저장 직전에도 검사해야 화면을 우회한 요청까지 막을 수 있다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 등록·수정 폼과 필수값·숫자 범위 검사

- **찾는 말:** 등록 · 수정 · 폼 · 필수값 · 입력 검증 · create · edit
- **언제 볼까:** 업무 항목을 입력하거나 기존 값을 수정하고 잘못된 입력을 저장 전에 알려줄 때
- **자료 형태:** 관리 화면 예제·UI 내부 구현 — 서버 연결은 별도
- **저장소·확인 버전:** [marmelab/react-admin](https://github.com/marmelab/react-admin) · [`0c33d9c3c27c`](https://github.com/marmelab/react-admin/commit/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a)

**먼저 볼 코드**

- [examples/simple/src/posts/PostCreate.tsx](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/examples/simple/src/posts/PostCreate.tsx) — `PostCreate, PostCreateToolbar, DependantInput`: 신규 생성, 기본값, 필수값·최솟값·최댓값 검사, 입력값에 따라 나타나는 항목, 저장 후 이동/계속 등록
- [examples/simple/src/posts/PostEdit.tsx](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/examples/simple/src/posts/PostEdit.tsx) — `PostEdit`: 기존 값 수정, required/number/minValue 검사, 중첩 배열 입력 및 미저장 변경 경고

**참고할 부분과 선정 이유:** PostCreate의 Create·SimpleFormConfigurable와 PostEdit의 Edit·TabbedForm을 비교한다. TextInput.validate와 NumberInput.validate가 업무 규칙을 적용할 지점이다. 입력 항목 source를 SPEC의 필드명에 맞추고, 저장 후 결과로 이동할지 폼을 초기화할지는 PostCreateToolbar의 onSuccess를 참고한다.

**함께 볼 파일**

- [examples/simple/src/index.tsx](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/examples/simple/src/index.tsx) — Admin에 데이터 공급자와 Resource를 연결하는 진입점
- [examples/simple/src/posts/index.tsx](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/examples/simple/src/posts/index.tsx) — list/create/edit/show 화면을 posts 자원에 연결
- [examples/simple/src/dataProvider.tsx](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/examples/simple/src/dataProvider.tsx) — 실제 서버가 아닌 fakeRestProvider 기반 예제 데이터 공급자; 실전 API 연결은 별도
- [examples/simple/package.json](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/examples/simple/package.json) — 예제 의존성과 개발·빌드 명령

**환경:** React 18·TypeScript·react-admin 5.15.5 계열·Material UI·react-hook-form. 확인한 examples/simple/package.json 기준이며, 예제는 모노레포 내부 패키지와 fake REST 데이터를 사용한다. 프로젝트의 채택 기술과 다르면 해당 흐름만 참고한다.

**한계·별도로 정할 것:** 프런트 입력 검증만으로 서버의 잘못된 요청을 차단할 수 없다. API에도 같은 필수값·타입·범위 검사가 필요하다. 예제의 권한·태그·번역·리치텍스트 등 부수 기능을 전부 도입할 필요는 없다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: MIT](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/LICENSE.md)

</details>

<a id="f-ui-save-inflight"></a>

### 2-2. 저장을 눌렀으면 끝날 때까지 다시 못 누르게 하기

**예시 상황**

예: 요청자가 R-001 수정 화면에서 저장을 눌렀지만 처리가 느려 같은 버튼을 다시 누르려고 한다.

**동작 예시**

1. 저장을 누른다 → 버튼을 잠시 누를 수 없게 바꾸고 저장 중임을 표시한다.
2. 저장이 끝나기 전에 다시 누르려 한다 → 같은 화면의 버튼은 반응하지 않는다.
3. 저장하는 쪽에서 입력 오류를 돌려준다 → 해당 입력칸에 오류를 보여주고 고칠 수 있게 한다.

**참고 코드가 제공하는 부분**

원본에서 저장 중 버튼을 막고 진행 표시를 보여주는 부분, 저장을 처리한 쪽이 돌려준 입력 오류를 화면에 붙이는 부분을 참고한다.

**따로 만들거나 정할 부분**

R-001의 실제 저장 결과를 받아 화면 상태를 바꾸는 연결이 필요하다. 다른 창에서도 같은 내용을 보내거나 통신이 끊겨 재전송되면 두 번 저장될 수 있으므로, 이를 막으려면 저장하는 쪽에서 같은 요청인지 확인하는 처리를 따로 만들어야 한다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 저장 중 버튼 비활성화·오류 표시

- **찾는 말:** 중복 제출 · 중복 클릭 · 저장 중 · 로딩 · isSubmitting
- **언제 볼까:** 저장 요청이 끝나기 전에 같은 버튼을 반복해서 누르는 실수를 줄일 때
- **자료 형태:** 관리 화면 예제·UI 내부 구현 — 서버 연결은 별도
- **저장소·확인 버전:** [marmelab/react-admin](https://github.com/marmelab/react-admin) · [`0c33d9c3c27c`](https://github.com/marmelab/react-admin/commit/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a)

**먼저 볼 코드**

- [packages/ra-ui-materialui/src/button/SaveButton.tsx](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/packages/ra-ui-materialui/src/button/SaveButton.tsx) — `SaveButton, disabled, handleSubmit, handleClick`: isSubmitting/isValidating를 사용한 버튼 비활성화, 저장 중 진행 표시, 서버 제출 오류를 폼에 반영

**참고할 부분과 선정 이유:** SaveButton의 disabled 계산과 isSubmitting에 따른 CircularProgress 표시를 함께 읽는다. handleSubmit은 saveContext.save를 기다린 뒤 반환된 필드 오류를 setSubmissionErrors로 연결한다. 이 패턴은 '대기 중/성공/실패' 상태가 있는 저장 버튼을 만들 때 참고한다.

**함께 볼 파일**

- [examples/simple/src/posts/PostCreate.tsx](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/examples/simple/src/posts/PostCreate.tsx) — PostCreateToolbar의 기본 submit 버튼과 type=button 저장 흐름
- [examples/simple/package.json](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/examples/simple/package.json) — react-hook-form 및 react-admin 의존성

**환경:** React 18·TypeScript·react-admin 5.15.5 계열·Material UI·react-hook-form. 확인한 examples/simple/package.json 기준이며, 예제는 모노레포 내부 패키지와 fake REST 데이터를 사용한다. 프로젝트의 채택 기술과 다르면 해당 흐름만 참고한다.

**한계·별도로 정할 것:** 이 소스가 다루는 것은 UI 중복 클릭 억제다. 새로고침·다른 창·네트워크 재시도로 발생하는 서버 중복 생성까지 보장하지 않는다. alwaysEnable 설정으로 기본 비활성화 규칙을 바꿀 수 있다. 서버 멱등성 구현은 이 항목의 범위 밖이다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: MIT](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/LICENSE.md)

</details>

<a id="f-ui-delete-confirm"></a>

### 2-3. 요청을 삭제하기 전에 한 번 더 확인하기

**예시 상황**

예: 요청자가 잘못 등록한 R-001을 삭제하려고 상세 화면의 삭제 버튼을 누른다.

**동작 예시**

1. 삭제를 누른다 → 'R-001을 삭제할까?' 같은 확인창을 띄우도록 만든다.
2. 취소를 누른다 → R-001은 그대로 남는다. 삭제 확인을 누르면 그때 삭제 처리를 요청한다.
3. 삭제가 성공한다 → 목록에서 R-001을 빼고 완료 안내를 보여준다. 실패하면 실패 안내를 보여준다.

**참고 코드가 제공하는 부분**

원본의 삭제 확인창과 삭제 성공·실패 후 화면 처리 흐름을 참고한다. 연결된 게시물 댓글을 함께 지우는 부분 예시도 있으나 모든 관련 자료를 안전하게 지우는 완성 기능은 아니다.

**따로 만들거나 정할 부분**

R-001을 실제로 지울지 삭제 표시만 남길지, 연결된 사진·처리 기록을 보관할지 함께 지울지 정해야 한다. 확인창에서 취소하는 것과 이미 삭제한 내용을 복구하는 것은 다르며, 삭제 후 복구는 이 예제에 포함되지 않는다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 삭제 전 확인과 성공·실패 후 화면 처리

- **찾는 말:** 삭제 · 삭제 확인 · 확인창 · delete
- **언제 볼까:** 목록 또는 상세 항목을 지우기 전에 대상과 행동을 확인시킬 때
- **자료 형태:** 관리 화면 예제·UI 내부 구현 — 서버 연결은 별도
- **저장소·확인 버전:** [marmelab/react-admin](https://github.com/marmelab/react-admin) · [`0c33d9c3c27c`](https://github.com/marmelab/react-admin/commit/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a)

**먼저 볼 코드**

- [packages/ra-ui-materialui/src/button/DeleteWithConfirmButton.tsx](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/packages/ra-ui-materialui/src/button/DeleteWithConfirmButton.tsx) — `DeleteWithConfirmButton, handleDialogOpen, handleDialogClose`: 확인창 상태, useDeleteController 호출, 성공 알림·선택 해제·이동, 실패 알림
- [examples/simple/src/dataProvider.tsx](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/examples/simple/src/dataProvider.tsx) — `beforeDelete`: 게시물 삭제 전에 관련 댓글을 조회해 deleteMany하고 쿼리 캐시를 무효화하는 예제

**참고할 부분과 선정 이유:** handleDialogOpen은 즉시 삭제하지 않고 확인창을 연다. Confirm.onConfirm에서 handleDelete를 호출하고 isPending을 표시하는 구조를 참고한다. 관련 데이터도 지워야 한다면 dataProvider의 beforeDelete를 읽되, 실제 연관 삭제 규칙은 과제에서 별도로 합의한다.

**함께 볼 파일**

- [examples/simple/src/index.tsx](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/examples/simple/src/index.tsx) — Resource와 데이터 공급자 컨텍스트
- [examples/simple/package.json](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/examples/simple/package.json) — react-admin·MUI 의존성

**환경:** React 18·TypeScript·react-admin 5.15.5 계열·Material UI·react-hook-form. 확인한 examples/simple/package.json 기준이며, 예제는 모노레포 내부 패키지와 fake REST 데이터를 사용한다. 프로젝트의 채택 기술과 다르면 해당 흐름만 참고한다.

**한계·별도로 정할 것:** 예제의 관련 댓글 삭제는 조회 perPage=100이며, DB 트랜잭션이나 무제한 연관 삭제 구현이 아니다. 실전의 보관·소프트삭제·복구 정책은 포함하지 않는다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: MIT](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/LICENSE.md)

</details>

<a id="category-3"></a>

## 3. 점검 파일을 가져오고 사진을 붙이고 결과를 내려받기

첨부는 요청 R-001에 'A-12 고장사진.jpg'를 붙여 나중에도 그 요청과 함께 볼 수 있게 하는 것이다. 표 파일 가져오기는 여러 검사 결과가 담긴 파일을 프로그램 안으로 읽어들이는 것이고, 내려받기는 반대로 '검사결과.csv'나 '결과.xlsx'를 본인 PC에 저장하는 것이다. 아래 자료는 이 과정의 서로 다른 부분을 다룬다.

<a id="f-file-csv-read-preview"></a>

### 3-1. CSV 파일에서 설비명과 측정값 읽기

**예시 상황**

예: 담당자가 파일 가져오기 화면에서 설비명·측정일·온도가 적힌 검사결과.csv를 선택한다.

**동작 예시**

1. 검사결과.csv를 고른다 → 파일 안의 열 이름과 각 행의 값을 읽는다.
2. 처음 5행만 읽도록 정한다 → 전체 내용을 처리하기 전에 일부 자료를 확인하는 데 쓸 수 있다.
3. 읽는 과정에서 형식 오류가 나온다 → 어떤 오류가 있었는지 받아서 사용자에게 보여주는 화면을 추가로 만든다.

**참고 코드가 제공하는 부분**

원본은 CSV 파일을 읽고 읽을 행 수·글자 인식 방법을 정하며 읽기 오류를 받는 예제다. CSV는 엑셀에서도 열 수 있는 글자 형태의 표 파일이고, .xlsx와는 다르다.

**따로 만들거나 정할 부분**

원본은 읽은 결과를 일반 사용자용 표로 보여주지 않는다. 읽은 설비명·온도를 화면에 표시하고, 검사 통과 후 어느 검사 기록에 저장할지 정하는 부분을 만들어야 한다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** CSV 가져오기·일부 행 읽기·오류 확인

- **찾는 말:** CSV · 가져오기 · import · 미리보기 · 인코딩 · 대용량
- **언제 볼까:** 사용자가 선택한 CSV를 읽고 열·행을 확인한 뒤 업무 데이터로 처리할 때
- **자료 형태:** 파일 처리 라이브러리·공식 예제 — 화면·저장 규칙을 과제에 맞춰 연결
- **저장소·확인 버전:** [mholt/PapaParse](https://github.com/mholt/PapaParse) · [`1fcb83c64acf`](https://github.com/mholt/PapaParse/commit/1fcb83c64acf61ae636b556b0eadeebaca0aea33)

**먼저 볼 코드**

- [player/player.js](https://github.com/mholt/PapaParse/blob/1fcb83c64acf61ae636b556b0eadeebaca0aea33/player/player.js) — `submit-parse click handler, buildConfig, stepFn, chunkFn, errorFn, completeFn`: 파일/텍스트 입력 분기, header/encoding/preview 옵션, 행·청크 단위 읽기, 오류·완료 처리
- [player/player.html](https://github.com/mholt/PapaParse/blob/1fcb83c64acf61ae636b556b0eadeebaca0aea33/player/player.html) — `#files, #preview, #header, #encoding`: 파일 선택과 파싱 설정을 연결하는 실제 데모 UI

**참고할 부분과 선정 이유:** buildConfig에서 header·encoding·preview를 어떻게 설정하는지 먼저 읽는다. preview는 읽을 행 수 제한이며, 완성된 표 미리보기 화면은 아니다. completeFn에 전달되는 결과의 data/errors를 화면에 표시하는 부분은 과제에서 구현한다. 큰 파일을 한꺼번에 읽지 않으려면 stepFn/chunkFn의 처리 경계를 참고한다.

**함께 볼 파일**

- [package.json](https://github.com/mholt/PapaParse/blob/1fcb83c64acf61ae636b556b0eadeebaca0aea33/package.json) — 확인한 라이브러리 버전 5.7.0 및 브라우저 엔트리

**환경:** 브라우저 JavaScript·PapaParse 5.7.0. 공식 player 데모는 jQuery를 사용한다. 그 데모의 UI 의존성과 새 프로젝트의 파싱 API 사용을 구분한다.

**한계·별도로 정할 것:** xlsx 바이너리를 읽는 예제가 아니다. 데모는 결과를 개발자 콘솔에 출력하며, 업무 검증·열 매핑·DB 저장은 구현하지 않는다. player.html의 외부 HTTP jQuery 링크는 배포 환경에 그대로 복사하지 않는다. 숫자로 보이는 식별자는 dynamicTyping 적용 전에 원문 보존 여부를 정한다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: MIT](https://github.com/mholt/PapaParse/blob/1fcb83c64acf61ae636b556b0eadeebaca0aea33/LICENSE)

</details>

<a id="f-file-xlsx-read-write"></a>

### 3-2. 엑셀 파일을 읽고 검사 결과를 새 엑셀 파일로 만들기

**예시 상황**

예: 담당자가 설비명·측정일·온도가 적힌 검사자료.xlsx를 받았다. 온도를 정한 기준과 비교한 뒤, 설비명·온도·판정이 담긴 결과.xlsx를 자신의 PC에 저장하려고 한다.

**동작 예시**

1. 검사자료.xlsx를 읽는다 → '검사결과' 시트에서 설비명 A-12와 온도 85 같은 값을 가져온다.
2. 온도를 판정하는 계산은 5-2번처럼 별도로 만든다고 가정한다. 그 결과가 '주의'라면 새 결과 시트에 'A-12 / 85 / 주의'를 한 행으로 넣는다.
3. '엑셀 내려받기'를 누른다 → 이 표가 들어 있는 결과.xlsx를 본인 PC에 저장하도록 다운로드 처리를 연결한다.

**참고 코드가 제공하는 부분**

원본에서 엑셀 파일을 읽고, 시트를 찾고, 셀 값을 다루고, 다시 파일로 쓰는 부분 예시를 참고한다. 온도를 판정하는 계산이나 위 다운로드 버튼·점검 업무 화면은 원본에 없고 별도로 만드는 부분이다.

**따로 만들거나 정할 부분**

업로드한 파일을 읽는 부분으로 넘기고, 완성된 엑셀 파일을 사용자 PC에 내려주는 화면·전송 처리를 붙여야 한다. 엑셀처럼 직접 편집하는 화면이나 수식 계산은 이 예제가 제공하지 않으며, 오래된 예제여서 현재 환경에서의 동작 확인도 필요하다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 엑셀 XLSX 읽기·셀 확인·결과 파일 쓰기

- **찾는 말:** 엑셀 · Excel · XLSX · 시트 · 셀 · 엑셀 내보내기
- **언제 볼까:** CSV가 아니라 여러 시트가 있는 XLSX를 읽거나 처리 결과를 XLSX로 만들 때
- **자료 형태:** 파일 처리 라이브러리·공식 예제 — 화면·저장 규칙을 과제에 맞춰 연결
- **저장소·확인 버전:** [exceljs/exceljs](https://github.com/exceljs/exceljs) · [`5bed18b45e82`](https://github.com/exceljs/exceljs/commit/5bed18b45e824f409b08456b59b87430ded023ab)

**먼저 볼 코드**

- [spec/integration/workbook/workbook.spec.js](https://github.com/exceljs/exceljs/blob/5bed18b45e824f409b08456b59b87430ded023ab/spec/integration/workbook/workbook.spec.js) — `Workbook > Serialise > xlsx file; sheets with correct names; empty string`: Workbook 생성·writeFile·readFile, 시트 이름 조회·셀 값 접근·행 추가의 실제 통합 테스트
- [lib/xlsx/xlsx.js](https://github.com/exceljs/exceljs/blob/5bed18b45e824f409b08456b59b87430ded023ab/lib/xlsx/xlsx.js) — `XLSX.readFile, XLSX.load, XLSX.writeFile, XLSX.writeBuffer`: 파일/버퍼 입력과 파일/버퍼 출력 구현

**참고할 부분과 선정 이유:** 완성 앱 대신 공식 테스트를 사용 예시로 읽는다. 가장 작은 'sheets with correct names' 테스트에서 addWorksheet·getCell.value·writeFile·readFile·getWorksheet 흐름을 본다. 서버에서 파일 경로를 다루면 readFile/writeFile, 브라우저 또는 메모리 데이터를 다루면 load/writeBuffer 경계를 확인한다. 업로드 UI와 다운로드 응답은 과제 코드에서 따로 연결한다.

**함께 볼 파일**

- [package.json](https://github.com/exceljs/exceljs/blob/5bed18b45e824f409b08456b59b87430ded023ab/package.json) — 4.4.0 버전과 Node/브라우저 엔트리·라이브러리 의존성

**환경:** ExcelJS package.json 4.4.0, JavaScript. readFile/writeFile은 Node 파일시스템용이다. 확인한 커밋은 2024-01-12로 오래되었으며 최신 환경 호환성·유지보수 상태를 보장하지 않는다.

**한계·별도로 정할 것:** 테스트 코드의 verquire·expect·testUtils는 해당 저장소 테스트 도구다. 그대로 앱에 복사하지 않는다. XLSX import/export 연결 예시이며 엑셀 편집기·수식 계산·완성된 미리보기 화면을 제공한다는 뜻이 아니다. 최신 채택 판단은 별도 확인이 필요하다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: MIT](https://github.com/exceljs/exceljs/blob/5bed18b45e824f409b08456b59b87430ded023ab/LICENSE)

</details>

<a id="f-file-attachment-upload"></a>

### 3-3. 점검 요청에 고장 사진을 첨부하고 보관하기

**예시 상황**

예: 요청자가 R-001의 첨부 영역에서 A-12 고장사진.jpg를 골라 요청과 함께 남기려고 한다.

**동작 예시**

1. 첨부할 사진을 고른다 → 선택한 파일이 전송 대상이 된다.
2. 업로드를 누른다 → 사진 파일을 프로그램이 보관하는 쪽으로 전송한다.
3. 받는 쪽이 파일을 저장한다 → 저장 결과를 화면에 돌려준다. 그 파일이 R-001의 첨부임을 기록하는 부분은 추가로 만든다.

**참고 코드가 제공하는 부분**

원본에는 파일 선택 화면, 파일 전송, 받는 쪽의 파일 저장 예제가 있다. 이 세 부분이 어떻게 이어지는지를 참고한다.

**따로 만들거나 정할 부분**

저장된 사진의 위치와 요청번호 R-001을 함께 기록해야 나중에 요청 화면에서 다시 찾을 수 있다. 누가 사진을 보거나 올릴 수 있는지, 어느 종류·크기까지 받을지, 어디에 보관할지와 전송 실패 안내도 따로 정해야 한다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 첨부파일 선택·전송과 서버 저장

- **찾는 말:** 첨부파일 · 업로드 · upload · multipart · 파일 저장
- **언제 볼까:** 사용자가 선택한 파일을 서버로 실제 전송하고 처리 결과를 받는 흐름이 필요할 때
- **자료 형태:** 파일 처리 라이브러리·공식 예제 — 화면·저장 규칙을 과제에 맞춰 연결
- **저장소·확인 버전:** [transloadit/uppy](https://github.com/transloadit/uppy) · [`921e8de58b9f`](https://github.com/transloadit/uppy/commit/921e8de58b9fb9df59943643a8bb2ef3bbe400b9)

**먼저 볼 코드**

- [examples/xhr-node/main.ts](https://github.com/transloadit/uppy/blob/921e8de58b9fb9df59943643a8bb2ef3bbe400b9/examples/xhr-node/main.ts) — `uppy, Dashboard, XHRUpload`: 파일 선택 대시보드와 HTTP 업로드 endpoint 연결
- [examples/xhr-node/server.ts](https://github.com/transloadit/uppy/blob/921e8de58b9fb9df59943643a8bb2ef3bbe400b9/examples/xhr-node/server.ts) — `http.createServer callback, form.parse`: POST /upload에서 multipart 요청을 파싱해 uploads 디렉터리에 저장하고 JSON 응답

**참고할 부분과 선정 이유:** main.ts의 XHRUpload.endpoint와 server.ts의 '/upload' 경로를 짝으로 읽는다. Dashboard는 선택 화면, XHRUpload는 전송, formidable은 서버 수신을 맡는다. 서버에서 file의 filepath·originalFilename·mimetype·size를 얻는 위치가 과제의 파일 검증·저장 기록과 연결될 지점이다.

**함께 볼 파일**

- [examples/xhr-node/package.json](https://github.com/transloadit/uppy/blob/921e8de58b9fb9df59943643a8bb2ef3bbe400b9/examples/xhr-node/package.json) — workspace:* Uppy 패키지, formidable, Vite 및 서버/클라이언트 실행 관계

**환경:** 브라우저 TypeScript + Node HTTP 서버 + formidable. Uppy 모노레포 내부 workspace:* 의존성으로 구성된 예제이며 독립 복사 후 바로 실행되는 패키지가 아니다. 버전은 고정 SHA를 기준으로 확인했다.

**한계·별도로 정할 것:** 예제는 개발용 CORS '*'·localhost:3020, 인증 없음, 오류에도 200을 반환한다. 실전에는 허용 출처·파일 크기/유형·접근 권한·오류 상태코드·보관 위치를 과제 조건에 맞춰 정해야 한다. Webcam은 필수 기능이 아니다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: MIT](https://github.com/transloadit/uppy/blob/921e8de58b9fb9df59943643a8bb2ef3bbe400b9/LICENSE)

</details>

<a id="f-file-preview-before-save"></a>

### 3-4. 사진을 올리기 전에 잘 골랐는지 확인하기

**예시 상황**

예: 요청자가 R-001 수정 화면에서 여러 사진을 고른 뒤, 그중 한 장을 잘못 선택했는지 확인하려고 한다.

**동작 예시**

1. 사진 두 장을 선택한다 → 선택한 사진을 화면에 보여준다.
2. 잘못 고른 사진 옆의 제거를 누른다 → 그 사진만 첨부 예정 목록에서 빠진다.
3. 남은 사진을 확인한 뒤 저장한다 → 실제 보관은 파일 전송·저장 처리와 연결해야 한다.

**참고 코드가 제공하는 부분**

원본에서 선택한 이미지를 보여주거나 파일 이름·링크를 표시하고 선택을 취소하는 부분을 참고한다. 사진을 서버에 저장하기 전, 현재 컴퓨터에서 선택한 파일을 확인하는 단계다.

**따로 만들거나 정할 부분**

화면에 사진이 보이는 것만으로 R-001에 보관된 것은 아니다. 남긴 파일을 전송해 저장하고 R-001과 연결해야 하며, PDF의 이름을 표시하는 것과 PDF 페이지 내용을 펼쳐 보여주는 것도 구분해야 한다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 선택한 첨부파일·이미지의 저장 전 확인

- **찾는 말:** 미리보기 · 이미지 · 파일 선택 · 첨부 삭제 · preview
- **언제 볼까:** 파일을 고른 뒤 저장하기 전에 어떤 파일을 첨부했는지 확인하거나 제거할 때
- **자료 형태:** 관리 화면 예제·UI 내부 구현 — 서버 연결은 별도
- **저장소·확인 버전:** [marmelab/react-admin](https://github.com/marmelab/react-admin) · [`0c33d9c3c27c`](https://github.com/marmelab/react-admin/commit/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a)

**먼저 볼 코드**

- [packages/ra-ui-materialui/src/input/FileInput.tsx](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/packages/ra-ui-materialui/src/input/FileInput.tsx) — `transformFile, onDrop, onRemove, FileInput`: 브라우저 File을 rawFile/src/title로 바꾸고 object URL 기반 표시, 선택·제거 및 크기/형식 옵션
- [examples/simple/src/posts/PostCreate.tsx](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/examples/simple/src/posts/PostCreate.tsx) — `PostCreate의 FileInput/FileField`: PDF 파일 선택과 파일 링크 표시
- [examples/simple/src/posts/PostEdit.tsx](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/examples/simple/src/posts/PostEdit.tsx) — `PostEdit의 ImageInput/ImageField`: 여러 이미지 선택과 이미지 표시

**참고할 부분과 선정 이유:** FileInput.transformFile이 만든 src는 로컬 파일을 가리키는 임시 object URL이다. PostCreate는 PDF 파일의 링크/이름 표시, PostEdit는 이미지 표시를 구성한다. 사용자가 파일을 제거하면 onRemove가 폼 값을 바꾸는 흐름을 참고한다.

**함께 볼 파일**

- [examples/simple/src/addUploadFeature.tsx](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/examples/simple/src/addUploadFeature.tsx) — 게시물 수정 시 새 그림만 Base64로 바꿔 기존 그림과 합치는 예제
- [examples/simple/src/dataProvider.tsx](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/examples/simple/src/dataProvider.tsx) — 업로드 변환 함수를 실제 dataProvider에 연결
- [examples/simple/package.json](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/examples/simple/package.json) — 예제 의존성

**환경:** React 18·TypeScript·react-admin 5.15.5 계열·Material UI·react-hook-form. 확인한 examples/simple/package.json 기준이며, 예제는 모노레포 내부 패키지와 fake REST 데이터를 사용한다. 프로젝트의 채택 기술과 다르면 해당 흐름만 참고한다.

**한계·별도로 정할 것:** object URL은 서버에 영구 저장된 URL이 아니다. PDF 페이지 렌더러는 이 항목에 없다. addUploadFeature는 posts 수정의 pictures만 처리하며 모든 파일·신규 등록의 영구 업로드를 보장하지 않는다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: MIT](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/LICENSE.md)

</details>

<a id="f-file-csv-export"></a>

### 3-5. 화면의 검사 결과를 CSV 파일로 내려받기

**예시 상황**

예: 담당자가 검사 결과 목록에서 설비명·측정일·판정 열을 파일로 받아 엑셀에서 열어보려고 한다.

**동작 예시**

1. 프로그램이 내보낼 열을 설비명·측정일·판정으로 정한다 → 예를 들어 'A-12 / 2026-10-29 / 주의'를 한 행으로 구성한다. 어떤 열을 넣을지는 구현할 때 정하는 예시이며, 열 선택 화면이 원본에 있다는 뜻은 아니다.
2. 'CSV 내려받기'를 누른다 → 정리한 표 내용을 파일로 만든다.
3. 검사결과.csv를 본인 PC에 저장한다 → 엑셀 등 표를 읽는 도구에서 열 수 있다.

**참고 코드가 제공하는 부분**

원본에서 여러 값이 들어 있는 자료를 출력할 열에 맞게 정리하고, CSV 파일을 만들어 내려받게 하는 흐름을 참고한다.

**따로 만들거나 정할 부분**

현재 보이는 행만 받을지 조건에 맞는 모든 행을 받을지 정하고, 해당 자료를 가져와 파일 생성 부분에 넘겨야 한다. 공개하면 안 되는 열을 빼고, 엑셀에서 수식으로 오해할 수 있는 값을 처리해야 하며, 색상이나 여러 시트는 CSV에 보존되지 않는다.

이름·연락처 열을 빼도 요청 내용이나 메모 속 개인정보는 남을 수 있다. 화면·내려받는 파일·로그·외부 전송 각각에서 누가 무엇을 볼 수 있는지, 어떤 내용을 가릴지 정하고 가짜 이름·연락처를 넣은 예시로 확인한다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 처리 결과를 CSV로 내려받기

- **찾는 말:** CSV 내보내기 · 결과 다운로드 · export · download
- **언제 볼까:** 목록·검사 결과를 사용자가 다른 도구에서 열 수 있는 CSV로 받을 때
- **자료 형태:** 관리 화면 예제·UI 내부 구현 — 서버 연결은 별도
- **저장소·확인 버전:** [marmelab/react-admin](https://github.com/marmelab/react-admin) · [`0c33d9c3c27c`](https://github.com/marmelab/react-admin/commit/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a)

**먼저 볼 코드**

- [examples/simple/src/posts/PostList.tsx](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/examples/simple/src/posts/PostList.tsx) — `exporter`: 중첩된 backlinks를 URL 배열로 바꾼 뒤 jsonExport→downloadCSV로 연결
- [packages/ra-core/src/export/downloadCSV.ts](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/packages/ra-core/src/export/downloadCSV.ts) — `downloadCSV`: CSV 문자열을 UTF-8 Blob으로 만들고 다운로드용 링크 클릭

**참고할 부분과 선정 이유:** exporter에서 행을 평평한 출력 구조로 바꾸는 부분을 먼저 참고한다. 업무에 필요한 열만 남기고 순서를 정한 뒤 CSV 문자열 생성과 파일 다운로드를 분리한다. downloadCSV는 브라우저 저장 트리거만 맡고 어떤 행을 내보낼지는 List/dataProvider 및 exporter가 정한다.

**함께 볼 파일**

- [examples/simple/package.json](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/examples/simple/package.json) — jsonexport 3.2 계열 의존성
- [examples/simple/src/dataProvider.tsx](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/examples/simple/src/dataProvider.tsx) — 내보낼 데이터 조회를 담당할 데이터 공급자

**환경:** React 18·TypeScript·react-admin 5.15.5 계열·Material UI·react-hook-form. 확인한 examples/simple/package.json 기준이며, 예제는 모노레포 내부 패키지와 fake REST 데이터를 사용한다. 프로젝트의 채택 기술과 다르면 해당 흐름만 참고한다.

**한계·별도로 정할 것:** 예제의 중첩 필드와 열 구성을 그대로 쓰지 않는다. 민감한 열 제거만으로 자유 문장 속 개인정보까지 가려지지는 않는다. 합의한 공개 범위에 따라 화면·파일·로그·외부 전송에 원문이 새어 나오지 않는지 별도로 검증한다. 엑셀 수식으로 해석될 수 있는 값 처리·대용량 출력·임시 URL 해제도 별도 적용·검증 항목이다. CSV는 XLSX 서식·다중 시트를 유지하지 않는다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: MIT](https://github.com/marmelab/react-admin/blob/0c33d9c3c27cc4bf97e11f56080c5bfe182f2f2a/LICENSE.md)

</details>

<a id="category-4"></a>

## 4. 가져온 검사표에서 빠진 값·중복·잘못된 숫자 찾기

검사결과.csv를 읽었다고 안의 값이 모두 올바른 것은 아니다. 예를 들어 설비명이 비었거나 같은 검사번호가 두 번 나오거나 온도 칸에 '오류'라는 글자가 있을 수 있다. 이 분류는 그런 행을 찾아 담당자가 확인할 수 있도록 만드는 데 쓸 계산 재료다.

<a id="f-data-invalid-rows"></a>

### 4-1. 설비명이 없거나 같은 검사번호가 반복된 행 찾기

**예시 상황**

예: 담당자가 가져온 검사표에서 설비명 없는 행과 검사번호가 두 번 나온 행을 확인하려고 한다.

**동작 예시**

1. 3행의 설비명이 비어 있다 → 3행을 '설비명 없음'으로 표시하도록 만든다.
2. 5행과 8행의 검사번호가 모두 C-001이다 → 두 행을 중복 후보로 고른다.
3. 고른 행의 원래 값과 행 번호를 오류 확인 표에 보여준다 → 담당자가 원본을 확인할 수 있게 한다.

**참고 코드가 제공하는 부분**

원본은 빈 값과 중복을 찾고 조건에 맞는 행을 골라내는 계산 방법을 제공한다. '설비명 없음'이라는 문구와 오류 확인 표는 그 재료를 조합해 우리가 만드는 부분이다.

**따로 만들거나 정할 부분**

검사번호만 같으면 중복인지, 설비명·검사일도 함께 같아야 중복인지 정해야 한다. 오류 행을 자동 삭제하지 말고 어떤 값을 고칠지 확인할 수 있게 하며, 공백만 들어간 칸도 빈 값으로 볼지는 별도로 처리해야 한다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 빈 값·중복·오류 행 골라내기

- **찾는 말:** 빈 값 · 누락 · 중복 · 오류 행 · CSV 검사
- **언제 볼까:** 표에서 문제가 있는 원본 행을 골라 사용자에게 보여줄 때
- **자료 형태:** 라이브러리 함수·사용 예제 — 업무용 검사표·판정 화면은 조합해서 구현
- **저장소·확인 버전:** [pandas-dev/pandas](https://github.com/pandas-dev/pandas) · [`c32acd3c8371`](https://github.com/pandas-dev/pandas/commit/c32acd3c8371a1e33936dea9009d8eef6822ee81)

**먼저 볼 코드**

- [pandas/core/frame.py](https://github.com/pandas-dev/pandas/blob/c32acd3c8371a1e33936dea9009d8eef6822ee81/pandas/core/frame.py#L8314-L8328) — `DataFrame.isna`: 결측값 판별과 빈 문자열·무한대 제외 설명
- [pandas/core/frame.py](https://github.com/pandas-dev/pandas/blob/c32acd3c8371a1e33936dea9009d8eef6822ee81/pandas/core/frame.py#L8963-L9103) — `DataFrame.duplicated`: subset/keep 설정, 중복된 모든 행을 찾는 keep=False 예제
- [pandas/core/indexing.py](https://github.com/pandas-dev/pandas/blob/c32acd3c8371a1e33936dea9009d8eef6822ee81/pandas/core/indexing.py#L371-L498) — `IndexingMixin.loc`: 조건으로 원본 행·열을 골라내는 예제

**참고할 부분과 선정 이유:** isna와 duplicated로 오류 여부를 True/False로 만든 뒤 loc으로 원본 행을 선택하는 부분을 참고한다. 행 번호·오류 이유를 함께 보여주는 검사표는 이 API들을 조합할 응용이다. 원본에 완성된 검사 화면이 있는 것은 아니다.

**함께 볼 파일**

- [doc/source/user_guide/missing_data.rst](https://github.com/pandas-dev/pandas/blob/c32acd3c8371a1e33936dea9009d8eef6822ee81/doc/source/user_guide/missing_data.rst) — 결측값 종류와 변환·채우기 설명
- [pyproject.toml](https://github.com/pandas-dev/pandas/blob/c32acd3c8371a1e33936dea9009d8eef6822ee81/pyproject.toml) — Python·패키지 요구사항

**환경:** Python + pandas. 확인한 개발 커밋의 pyproject.toml은 Python >=3.11. 개발 브랜치 설치를 권하는 자료가 아니며 실전 설치 버전에서 사용할 API를 다시 확인한다.

**한계·별도로 정할 것:** 빈 문자열·공백·무한대는 isna만으로 모두 검출되지 않는다. 중복 기준 열과 제거/유지 정책은 과제에서 정한다. 자동 삭제·채우기를 임의 적용하지 않는다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: BSD-3-Clause](https://github.com/pandas-dev/pandas/blob/c32acd3c8371a1e33936dea9009d8eef6822ee81/LICENSE)

</details>

<a id="f-data-convert"></a>

### 4-2. 온도·날짜를 계산할 수 있게 바꾸고 실패한 값 찾기

**예시 상황**

예: 가져온 표의 온도는 글자 '85'로 적혀 있고, 측정일은 '2026/10/29'처럼 적혀 있어 같은 형식으로 맞추려고 한다.

**동작 예시**

1. 온도 칸의 '85'를 읽는다 → 계산에 쓸 숫자 85로 바꾼다.
2. 측정일 '2026/10/29'를 정한 날짜 형식에 맞춰 읽는다 → 날짜순 정렬과 기간 계산에 쓸 수 있는 값으로 바꾼다.
3. 온도 칸에 '고장'이 적힌 행을 만난다 → 숫자로 바꾸지 못한 행으로 따로 고르고 원래 글자를 남긴다.

**참고 코드가 제공하는 부분**

원본에서 글자를 숫자나 날짜로 바꾸고, 바꿀 수 없는 값을 찾아내는 방법을 참고한다. 어떤 열을 바꾸고 실패를 어떻게 보여줄지는 점검표에 맞춰 만드는 부분이다.

**따로 만들거나 정할 부분**

바꾸기 전 값과 바꾼 값을 함께 남기고 실패 건수·행 번호를 보여주어야 한다. 접수번호 '001'을 숫자 1로 바꾸면 안 되는 경우처럼, 숫자로 보이더라도 그대로 보존할 열을 정해야 한다.

과거 특정 시점의 판단을 재현하는 과제라면 기준 시각과 시간대를 입력값으로 정하고, 그때 알 수 없었던 답변·사후 결과는 사용하지 않는다. 사건이 일어난 시각과 그 정보가 기록되어 확인 가능해진 시각은 다를 수 있다. 날짜 형식만 바꾼다고 이 구분이 자동으로 되는 것은 아니다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 숫자·날짜 통일과 변환 실패 찾기

- **찾는 말:** 숫자 변환 · 자료형 · 날짜 · 시간대 · 단위 · 파싱 오류
- **언제 볼까:** 문자열 숫자와 섞인 날짜 형식을 계산 전에 정리할 때
- **자료 형태:** 라이브러리 함수·사용 예제 — 업무용 검사표·판정 화면은 조합해서 구현
- **저장소·확인 버전:** [pandas-dev/pandas](https://github.com/pandas-dev/pandas) · [`c32acd3c8371`](https://github.com/pandas-dev/pandas/commit/c32acd3c8371a1e33936dea9009d8eef6822ee81)

**먼저 볼 코드**

- [pandas/core/tools/numeric.py](https://github.com/pandas-dev/pandas/blob/c32acd3c8371a1e33936dea9009d8eef6822ee81/pandas/core/tools/numeric.py#L52-L210) — `to_numeric`: 문자열 숫자/잘못된 값 변환 예제와 오류 정책
- [pandas/core/tools/datetimes.py](https://github.com/pandas-dev/pandas/blob/c32acd3c8371a1e33936dea9009d8eef6822ee81/pandas/core/tools/datetimes.py#L847-L975) — `to_datetime`: format/utc/unit/origin 옵션
- [pandas/core/tools/datetimes.py](https://github.com/pandas-dev/pandas/blob/c32acd3c8371a1e33936dea9009d8eef6822ee81/pandas/core/tools/datetimes.py#L1100-L1160) — `to_datetime Examples`: 변환 불가 날짜와 혼합 시간대 예제

**참고할 부분과 선정 이유:** apple이 포함된 숫자 변환 예제와 잘못된 날짜→NaT 예제를 먼저 본다. 원본 열을 보존하고 변환 후 결측값을 찾아 오류 행을 표시하는 방식으로 응용한다. unit은 숫자형 시각의 초/밀리초 등 시간 단위를 지정하는 옵션이며 물리량 단위 자동 변환 기능은 아니다.

**함께 볼 파일**

- [pandas/core/indexing.py](https://github.com/pandas-dev/pandas/blob/c32acd3c8371a1e33936dea9009d8eef6822ee81/pandas/core/indexing.py#L458-L498) — 변환 실패 행 선택
- [pyproject.toml](https://github.com/pandas-dev/pandas/blob/c32acd3c8371a1e33936dea9009d8eef6822ee81/pyproject.toml) — Python·패키지 요구사항

**환경:** Python + pandas. 확인한 개발 커밋의 pyproject.toml은 Python >=3.11. 개발 브랜치 설치를 권하는 자료가 아니며 실전 설치 버전에서 사용할 API를 다시 확인한다.

**한계·별도로 정할 것:** coerce로 실패를 결측으로 바꾸면 실패 건수를 별도 보고해야 한다. ID의 앞자리 0, 시간대 없는 지역 시각, 숫자 정밀도 손실에 주의한다. utc=True가 원래 지역 시간대를 추론하지는 않는다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: BSD-3-Clause](https://github.com/pandas-dev/pandas/blob/c32acd3c8371a1e33936dea9009d8eef6822ee81/LICENSE)

</details>

**아직 준비되지 않은 부분**

- 온도가 섭씨인지 화씨인지, 무게가 kg인지 g인지 자료에서 자동으로 알아내고 맞춰주는 완성 예제는 아직 없다. 입력 단위가 무엇인지 확인하고 변환 규칙을 따로 정해야 한다.

<a id="category-5"></a>

## 5. 점검 값으로 점수·판정·처리 순서 계산하기

이 분류의 계산은 사람이 합의한 기준을 프로그램에 넣는 방식이다. 예를 들어 '온도 80도 이상이면 주의'라는 기준을 정하면 A-12의 온도 85도에 같은 판정이 나오게 만든다. 아래 숫자와 기준은 설명을 위한 가정이며 실제 설비의 안전 기준이나 시험 요구사항이 아니다.

<a id="f-rules-weighted-score"></a>

### 5-1. 긴급도와 영향도를 합쳐 종합 점수 계산하기

**예시 상황**

예: R-001의 긴급도 80점과 영향도 60점을 각각 70%, 30% 비중으로 반영하려고 한다.

**동작 예시**

1. 긴급도 80, 영향도 60을 입력값으로 받는다 → 두 항목 모두 100점 기준이라고 가정한다.
2. 80×0.7 + 60×0.3을 계산한다 → 종합 점수 74가 나온다.
3. R-001 옆에 종합 점수 74를 표시하도록 만든다 → 실제 표시 화면은 추가로 만든다.

**참고 코드가 제공하는 부분**

원본에서 항목별 비중을 반영해 평균을 계산하는 부분을 참고한다. 긴급도·영향도라는 항목이나 점수표가 제공되는 것은 아니다.

**따로 만들거나 정할 부분**

긴급도와 영향도를 누가 어떤 기준으로 매길지, 비중을 얼마로 할지 정해야 한다. 빈 점수 처리·반올림·서로 다른 점수 범위를 맞추는 규칙을 정하고, 계산 결과를 어느 요청에 붙일지도 연결해야 한다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 가중 점수 계산

- **찾는 말:** 점수 · 가중치 · 가중 평균 · 우선순위 점수
- **언제 볼까:** 여러 수치를 정해진 비중으로 종합할 때
- **자료 형태:** 라이브러리 함수·사용 예제 — 업무용 검사표·판정 화면은 조합해서 구현
- **저장소·확인 버전:** [numpy/numpy](https://github.com/numpy/numpy) · [`9e2409c6bb6e`](https://github.com/numpy/numpy/commit/9e2409c6bb6ee5814d139f436f93f587e03cf9ed)

**먼저 볼 코드**

- [numpy/lib/_function_base_impl.py](https://github.com/numpy/numpy/blob/9e2409c6bb6ee5814d139f436f93f587e03cf9ed/numpy/lib/_function_base_impl.py#L452-L613) — `average`: 가중 평균 공식·행별 가중치 예제·가중치 합 0 검사

**참고할 부분과 선정 이유:** average의 axis=1, weights 예제와 구현부의 곱셈→합계→나눗셈을 참고한다. 원본은 가중 평균이며, 업무 점수표·정규화·반올림 기준은 과제에서 정한다.

**함께 볼 파일**

- [pyproject.toml](https://github.com/numpy/numpy/blob/9e2409c6bb6ee5814d139f436f93f587e03cf9ed/pyproject.toml) — Python·패키지 요구사항

**환경:** Python + NumPy. 확인한 개발 커밋은 Python >=3.12. API 사용 예제를 참고하며 라이브러리 내부 구현을 통째로 복사하지 않는다.

**한계·별도로 정할 것:** 가중 합과 가중 평균은 다르다. 단위·범위가 다른 값을 바로 평균 내지 않도록 기준을 정한다. 결측값·가중치 합 0·동점 정책은 별도로 필요하다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: BSD-3-Clause](https://github.com/numpy/numpy/blob/9e2409c6bb6ee5814d139f436f93f587e03cf9ed/LICENSE.txt)

</details>

<a id="f-rules-condition-reason"></a>

### 5-2. 측정값을 기준과 비교해 정상·주의·위험으로 나누고 이유 붙이기

**예시 상황**

예: A-12의 온도 85도를 읽어 설명용 기준에 따라 정상·주의·위험 중 하나를 표시하려고 한다.

**동작 예시**

1. 설명용으로 '90도 이상 위험, 80도 이상 90도 미만 주의, 80도 미만 정상'을 정한다 → 조건 순서와 경계를 고정한다.
2. 85도를 넣는다 → 해당 조건에 따라 '주의'가 선택된다.
3. '주의: 80도 이상 90도 미만'이라고 화면에 보여주도록 만든다 → 이유 문구는 같은 조건에 맞춰 추가한다.

**참고 코드가 제공하는 부분**

원본은 여러 조건을 순서대로 확인해 맞는 결과를 고르는 계산 방법이다. 정상·주의·위험이라는 업무 판정과 이유 문구는 그 방법을 이용해 만드는 부분이다.

**따로 만들거나 정할 부분**

실제 과제의 기준값을 받아 조건에 넣고, 정확히 80도나 90도일 때의 결과도 정해야 한다. 값이 비었거나 측정 오류일 때는 정상으로 처리하지 않도록 별도 결과를 정하고 화면에 연결해야 한다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 기준값 비교·조건별 분류·판정 이유

- **찾는 말:** 조건 · 판정 · 분류 · 기준값 · threshold · 판정 이유
- **언제 볼까:** 온도·점수·기한 등에 따라 정상/주의/위험을 분류할 때
- **자료 형태:** 라이브러리 함수·사용 예제 — 업무용 검사표·판정 화면은 조합해서 구현
- **저장소·확인 버전:** [numpy/numpy](https://github.com/numpy/numpy) · [`9e2409c6bb6e`](https://github.com/numpy/numpy/commit/9e2409c6bb6ee5814d139f436f93f587e03cf9ed)

**먼저 볼 코드**

- [numpy/lib/_function_base_impl.py](https://github.com/numpy/numpy/blob/9e2409c6bb6ee5814d139f436f93f587e03cf9ed/numpy/lib/_function_base_impl.py#L825-L933) — `select`: condlist/choicelist/default와 첫 조건 우선 처리

**참고할 부분과 선정 이유:** 조건 목록과 결과 목록을 연결하는 예제를 참고한다. 여러 조건에 맞으면 앞쪽 조건을 선택한다. 같은 조건 목록에 상태명과 이유 문구를 연결하는 것은 이 코드로부터의 응용이다. 원본은 숫자 결과 선택 예제이며 완성된 업무 판정 화면·감사 기록이 아니다.

**함께 볼 파일**

- [numpy/lib/_function_base_impl.py](https://github.com/numpy/numpy/blob/9e2409c6bb6ee5814d139f436f93f587e03cf9ed/numpy/lib/_function_base_impl.py#L698-L815) — 조건마다 다른 계산식을 적용할 때 piecewise 예제
- [pyproject.toml](https://github.com/numpy/numpy/blob/9e2409c6bb6ee5814d139f436f93f587e03cf9ed/pyproject.toml) — Python·패키지 요구사항

**환경:** Python + NumPy. 확인한 개발 커밋은 Python >=3.12. API 사용 예제를 참고하며 라이브러리 내부 구현을 통째로 복사하지 않는다.

**한계·별도로 정할 것:** 기준값·경계의 = 포함 여부·결측값·미해당 기본값은 별도로 정한다. 문자열 결과는 default도 호환되는 자료형이어야 한다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: BSD-3-Clause](https://github.com/numpy/numpy/blob/9e2409c6bb6ee5814d139f436f93f587e03cf9ed/LICENSE.txt)

</details>

<a id="f-rules-priority-sort"></a>

### 5-3. 점수가 높고 기한이 가까운 요청부터 줄 세우기

**예시 상황**

예: 담당자가 R-001과 R-002 중 무엇을 먼저 처리할지 정해진 규칙대로 목록에 표시하려고 한다.

**동작 예시**

1. R-001은 74점·10월 30일 기한, R-002는 90점·10월 31일 기한이라고 가정한다 → 점수가 높은 순이면 R-002가 먼저 온다.
2. 다른 요청도 90점이면 기한을 비교한다 → 기한이 더 빠른 요청을 앞에 둔다.
3. 점수와 기한도 같으면 접수번호로 순서를 정한다 → 반복해서 조회해도 같은 순서가 되도록 만든다.

**참고 코드가 제공하는 부분**

원본에서 여러 열을 순서대로 비교해 자료를 정렬하는 방법을 참고한다. 점수 계산이나 우리 업무의 우선순위 기준을 제공하는 것은 아니다.

**따로 만들거나 정할 부분**

요청마다 계산된 점수·기한·접수번호를 정렬 부분에 넘기고 결과 순서대로 표를 그려야 한다. 점수가 없는 요청의 위치, 높은 점수와 가까운 기한 중 무엇을 먼저 볼지부터 정해야 한다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 점수·기한에 따른 처리 순서

- **찾는 말:** 우선순위 · 순위 · 정렬 · 동점 · 마감일
- **언제 볼까:** 점수가 높은 순서, 동점이면 기한·접수순으로 정렬할 때
- **자료 형태:** 라이브러리 함수·사용 예제 — 업무용 검사표·판정 화면은 조합해서 구현
- **저장소·확인 버전:** [pandas-dev/pandas](https://github.com/pandas-dev/pandas) · [`c32acd3c8371`](https://github.com/pandas-dev/pandas/commit/c32acd3c8371a1e33936dea9009d8eef6822ee81)

**먼저 볼 코드**

- [pandas/core/frame.py](https://github.com/pandas-dev/pandas/blob/c32acd3c8371a1e33936dea9009d8eef6822ee81/pandas/core/frame.py#L9134-L9340) — `DataFrame.sort_values`: 여러 열 정렬·오름/내림차순·결측 배치 예제

**참고할 부분과 선정 이유:** 여러 열 정렬 예제의 키를 점수·기한·고유 접수번호로 바꿔 적용한다. 점수 계산은 별도이며 어떤 순서가 공정한지는 이 코드가 정하지 않는다.

**함께 볼 파일**

- [pandas/core/tools/datetimes.py](https://github.com/pandas-dev/pandas/blob/c32acd3c8371a1e33936dea9009d8eef6822ee81/pandas/core/tools/datetimes.py#L847-L975) — 기한을 날짜로 변환
- [pyproject.toml](https://github.com/pandas-dev/pandas/blob/c32acd3c8371a1e33936dea9009d8eef6822ee81/pyproject.toml) — Python·패키지 요구사항

**환경:** Python + pandas. 확인한 개발 커밋의 pyproject.toml은 Python >=3.11. 개발 브랜치 설치를 권하는 자료가 아니며 실전 설치 버전에서 사용할 API를 다시 확인한다.

**한계·별도로 정할 것:** 동점 순서가 중요하면 추가 키를 명시한다. DataFrame의 stable 옵션은 단일 열 정렬에 적용되는 제약이 있다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: BSD-3-Clause](https://github.com/pandas-dev/pandas/blob/c32acd3c8371a1e33936dea9009d8eef6822ee81/LICENSE)

</details>

<a id="category-6"></a>

## 6. 누가 맡을지 정하고 승인·반려 기록하기

요청자와 담당자는 다를 수 있다. 예를 들어 요청자가 R-001을 등록하면 관리자가 담당자 김담당에게 점검을 맡기고, 승인 담당자가 처리 결과를 검토하는 흐름을 생각할 수 있다. 실제 과제에 승인 단계가 없다면 아래 승인 기능을 추가할 이유는 없으며, 여기서는 필요한 경우 참고할 부분을 설명한다.

<a id="f-6-1"></a>

### 6-1. 요청 담당자를 정하고 완료 여부 남기기

**예시 상황**

예: 관리자가 R-001 상세 화면에서 점검 담당자를 김담당으로 정하려고 한다.

**동작 예시**

1. 담당자로 김담당을 선택하고 배정한다 → R-001에 연결된 김담당의 할 일을 만든다.
2. 김담당이 자신의 할 일을 끝냈다고 표시한다 → 배정된 할 일이 완료로 바뀌고 처리 내역을 남긴다.
3. 배정을 취소한다 → 그 사람에게 배정된 할 일을 해제하고 변경 내역을 남긴다.

**참고 코드가 제공하는 부분**

원본에서 업무 문서와 담당자의 할 일을 연결하고, 배정·완료·해제 시 원문서의 담당자 표시와 기록을 갱신하는 부분을 참고한다. 큰 업무 프로그램 안의 코드라 일부 파일만 옮겨 바로 쓰는 예제는 아니다.

**따로 만들거나 정할 부분**

우리 요청번호 R-001과 담당자 계정을 연결해 배정 내용을 저장해야 한다. 담당자의 할 일 완료가 곧 요청 전체 완료인지도 정해야 하며, 담당자에게 배정했다는 이유만으로 다른 비공개 자료까지 보이게 해서는 안 된다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 담당자 배정·완료·해제와 처리 이력

- **찾는 말:** 담당자 · 배정 · 할 일 · 완료 · 배정 해제 · 처리 이력
- **언제 볼까:** 요청이나 점검 항목을 담당자에게 배정하고 누가 맡았는지·끝냈는지 표시할 때.
- **자료 형태:** 큰 업무 프레임워크의 구현 — 데이터·권한 구조와 함께 참고
- **저장소·확인 버전:** [frappe/frappe](https://github.com/frappe/frappe) · [`667fbb59e429`](https://github.com/frappe/frappe/commit/667fbb59e429e45592f02373729188d1c62d2a47)

**먼저 볼 코드**

- [frappe/desk/form/assign_to.py](https://github.com/frappe/frappe/blob/667fbb59e429e45592f02373729188d1c62d2a47/frappe/desk/form/assign_to.py) — `add / _add / close / set_status`: 배정할 문서와 사용자로 열린 ToDo를 만들고 완료·취소 상태를 반영한다.
- [frappe/desk/doctype/todo/todo.py](https://github.com/frappe/frappe/blob/667fbb59e429e45592f02373729188d1c62d2a47/frappe/desk/doctype/todo/todo.py#L43-L143) — `ToDo.validate / on_update / add_assign_comment / update_in_reference`: 배정·상태 변경 시 원래 문서에 댓글 이력을 남기고 현재 담당자 목록을 갱신한다.

**참고할 부분과 선정 이유:** AI는 assign_to.py에서 먼저 ‘문서 종류+문서 ID+담당자+Open 상태’로 중복 배정을 찾는 부분을 읽는다. 이후 ToDo를 별도 기록으로 만들고 원문서의 담당자 표시를 갱신하는 연결을 참고한다. close는 현재 로그인한 담당자만 완료하도록 검사하고, set_status는 Closed/Cancelled로 바꾼다. todo.py에서는 변경 전 상태와 새 상태를 비교해 배정 이력을 만드는 부분을 참고한다. 업무 자체의 진행 상태와 ‘배정된 할 일의 상태’를 구분해 우리 데이터에 맞춘다.

**함께 볼 파일**

- [frappe/permissions.py](https://github.com/frappe/frappe/blob/667fbb59e429e45592f02373729188d1c62d2a47/frappe/permissions.py) — 원문서 접근 권한 검사
- [pyproject.toml](https://github.com/frappe/frappe/blob/667fbb59e429e45592f02373729188d1c62d2a47/pyproject.toml) — 실행 환경과 프레임워크 의존성

**환경:** Python·JavaScript 기반 Frappe 전체 프레임워크 코드. 이 커밋 pyproject.toml은 Python >=3.14,<3.15와 DB 드라이버·Redis·RQ 등을 요구한다. 개별 함수만 복사해 실행할 수 있는 독립 예제가 아니다.

**한계·별도로 정할 것:** 배정할 때 읽기 권한이 없으면 문서를 공유하는 분기가 있다. 이를 그대로 가져오면 접근 범위가 넓어질 수 있으므로 과제의 권한 규칙에 맞게 재설계해야 한다. 중복 조회가 곧 동시 요청의 유일성 보장은 아니다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: MIT](https://github.com/frappe/frappe/blob/667fbb59e429e45592f02373729188d1c62d2a47/LICENSE)

</details>

<a id="f-6-2"></a>

### 6-2. 내가 검토할 승인 대기 요청만 모아 보기

**예시 상황**

예: 승인 담당자 박승인이 '내 승인 대기' 화면에서 자신이 처리할 R-001을 찾으려고 한다.

**동작 예시**

1. 박승인이 자신의 계정으로 접속한다 → 그 사람에게 허용된 역할과 아직 끝나지 않은 승인 건을 확인한다.
2. 승인 가능한 미완료 요청만 목록에 보여준다 → 다른 사람만 처리할 수 있는 요청을 섞지 않도록 만든다.
3. R-001을 누른다 → 검토해야 할 원래 요청 내용을 연다. 처리가 끝나면 누가 완료했는지 남긴다.

**참고 코드가 제공하는 부분**

원본에서 사용자의 역할과 승인 대기 상태를 함께 확인해 목록을 제한하고, 대기 항목을 원래 문서와 연결하는 방식을 참고한다.

**따로 만들거나 정할 부분**

누가 어떤 요청을 승인할 수 있는지 규칙을 정하고, R-001이 승인 대기 상태가 될 때 목록에 올릴 기록을 만들어야 한다. 목록에서 숨긴 자료라도 주소를 직접 열면 보이지 않도록, 요청 상세 화면의 접근 제한도 따로 연결해야 한다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 내가 처리할 승인 대기 목록

- **찾는 말:** 승인 대기 · 결재함 · 미처리 · 승인자 · 권한별 목록
- **언제 볼까:** 현재 사용자가 처리할 수 있는 미완료 승인 요청만 모아 보여줄 때.
- **자료 형태:** 큰 업무 프레임워크의 구현 — 데이터·권한 구조와 함께 참고
- **저장소·확인 버전:** [frappe/frappe](https://github.com/frappe/frappe) · [`667fbb59e429`](https://github.com/frappe/frappe/commit/667fbb59e429e45592f02373729188d1c62d2a47)

**먼저 볼 코드**

- [frappe/workflow/doctype/workflow_action/workflow_action.py](https://github.com/frappe/frappe/blob/667fbb59e429e45592f02373729188d1c62d2a47/frappe/workflow/doctype/workflow_action/workflow_action.py) — `get_permission_query_conditions / create_workflow_actions_for_roles / update_completed_workflow_actions_using_role`: 허용 역할과 Open 상태로 목록을 제한하고 완료한 사람·역할·시각을 기록한다.
- [frappe/workflow/doctype/workflow_action/workflow_action_list.js](https://github.com/frappe/frappe/blob/667fbb59e429e45592f02373729188d1c62d2a47/frappe/workflow/doctype/workflow_action/workflow_action_list.js#L1-L17) — `get_form_link`: 열린 승인 항목을 원래 업무 문서 상세 화면으로 연결한다.

**참고할 부분과 선정 이유:** 승인 대상 업무 문서와 승인할 사람에게 보이는 대기 항목을 별도 레코드로 관리하는 구조를 참고한다. get_permission_query_conditions는 현재 사용자의 역할과 Workflow Action Permitted Role을 연결하고 status='Open' 조건을 붙인다. 승인 후에는 update_completed_workflow_actions_using_role이 Completed와 completed_by/completed_by_role을 기록한다. 화면 링크는 승인 기록 자체보다 실제 검토할 원문서로 연결한다.

**함께 볼 파일**

- [frappe/model/workflow.py](https://github.com/frappe/frappe/blob/667fbb59e429e45592f02373729188d1c62d2a47/frappe/model/workflow.py) — 상태별 가능한 작업과 승인 권한 계산
- [frappe/workflow/doctype/workflow/workflow.json](https://github.com/frappe/frappe/blob/667fbb59e429e45592f02373729188d1c62d2a47/frappe/workflow/doctype/workflow/workflow.json) — 상태·전환·대상 문서 설정 구조

**환경:** Python·JavaScript 기반 Frappe 전체 프레임워크 코드. 이 커밋 pyproject.toml은 Python >=3.14,<3.15와 DB 드라이버·Redis·RQ 등을 요구한다. 개별 함수만 복사해 실행할 수 있는 독립 예제가 아니다.

**한계·별도로 정할 것:** 관리자는 목록 조건의 예외다. 단순히 모든 Open 레코드를 조회하는 코드로 바꾸면 다른 사람의 승인 건이 노출될 수 있다. 이 목록 필터만으로 업무 문서의 모든 접근 권한이 해결되는 것은 아니다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: MIT](https://github.com/frappe/frappe/blob/667fbb59e429e45592f02373729188d1c62d2a47/LICENSE)

</details>

<a id="f-6-3"></a>

### 6-3. 요청을 승인하거나 반려하고 누가 했는지 남기기

**예시 상황**

예: 박승인이 R-001의 점검 결과를 읽고 승인하거나 요청자에게 다시 보내려고 한다.

**동작 예시**

1. R-001을 연다 → 현재 상태와 박승인의 권한에 따라 할 수 있는 동작을 보여준다.
2. 승인 또는 반려를 누른다 → 저장된 최신 상태와 권한을 다시 확인한 뒤 허용된 상태로만 바꾼다.
3. 처리가 끝난다 → R-001의 상태와 처리 이력을 남긴다. 본인 요청을 직접 승인하지 못하게 제한하는 방법도 참고할 수 있다.

**참고 코드가 제공하는 부분**

원본에서 가능한 다음 상태를 정하고, 버튼을 누른 사람에게 실제 권한이 있는지 다시 검사한 뒤 상태를 저장하는 흐름을 참고한다. 화면에서 버튼을 안 보이게 하는 것과 실제 잘못된 처리를 거절하는 것을 함께 다룬다.

**따로 만들거나 정할 부분**

우리 업무의 대기·승인·반려 상태, 각 동작을 허용할 사람, 자기 승인 여부를 정해야 한다. 반려 사유를 반드시 적게 하려면 입력칸을 만들고 빈 사유를 거절하며 R-001의 기록에 사유를 저장하는 부분을 추가해야 한다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 승인·반려·상태 전환과 전환 이력

- **찾는 말:** 승인 · 반려 · 상태 변경 · 자기 승인 금지 · 단계 · 결재 이력
- **언제 볼까:** 대기→승인 또는 대기→반려처럼 허용된 다음 상태로만 이동해야 할 때.
- **자료 형태:** 큰 업무 프레임워크의 구현 — 데이터·권한 구조와 함께 참고
- **저장소·확인 버전:** [frappe/frappe](https://github.com/frappe/frappe) · [`667fbb59e429`](https://github.com/frappe/frappe/commit/667fbb59e429e45592f02373729188d1c62d2a47)

**먼저 볼 코드**

- [frappe/model/workflow.py](https://github.com/frappe/frappe/blob/667fbb59e429e45592f02373729188d1c62d2a47/frappe/model/workflow.py#L77-L273) — `get_transitions / apply_workflow / has_approval_access`: 서버에서 현재 상태·역할·조건을 확인한 뒤 다음 상태를 저장하고 Workflow 댓글 이력을 남긴다.
- [frappe/public/js/frappe/form/workflow.js](https://github.com/frappe/frappe/blob/667fbb59e429e45592f02373729188d1c62d2a47/frappe/public/js/frappe/form/workflow.js#L84-L149) — `FormStates.show_actions / handle_workflow_action`: 사용 가능한 작업 버튼을 만들고 apply_workflow를 호출한다.

**참고할 부분과 선정 이유:** 먼저 workflow.json의 states와 transitions를 보고 ‘현재 상태·작업 이름·허용 역할·다음 상태’를 분리한다. apply_workflow는 화면이 보내온 상태를 신뢰하지 않고 문서를 DB에서 다시 읽으며, get_transitions로 허용된 작업인지 검사한다. 승인과 반려는 서로 다른 action/next_state로 설정하는 방식이다. has_approval_access의 자기 승인 제한과 저장 후 doc.add_comment('Workflow', ...)를 참고한다. UI에서 버튼 숨기기와 서버에서 거절하기를 함께 적용하는 흐름이다.

**함께 볼 파일**

- [frappe/workflow/doctype/workflow/workflow.json](https://github.com/frappe/frappe/blob/667fbb59e429e45592f02373729188d1c62d2a47/frappe/workflow/doctype/workflow/workflow.json) — 프로젝트에 맞게 정의해야 하는 상태와 전환표
- [frappe/workflow/doctype/workflow_action/workflow_action.py](https://github.com/frappe/frappe/blob/667fbb59e429e45592f02373729188d1c62d2a47/frappe/workflow/doctype/workflow_action/workflow_action.py) — 대기 항목 생성·완료 기록
- [frappe/model/document.py](https://github.com/frappe/frappe/blob/667fbb59e429e45592f02373729188d1c62d2a47/frappe/model/document.py) — 문서 저장·제출·취소와 권한 처리

**환경:** Python·JavaScript 기반 Frappe 전체 프레임워크 코드. 이 커밋 pyproject.toml은 Python >=3.14,<3.15와 DB 드라이버·Redis·RQ 등을 요구한다. 개별 함수만 복사해 실행할 수 있는 독립 예제가 아니다.

**한계·별도로 정할 것:** 승인/반려 버튼 이름과 규칙은 프로젝트가 설정해야 한다. 문서의 saved/submitted/cancelled 상태와 업무의 승인/반려 상태는 같은 개념이 아니다. 반려 사유 필수입력 같은 요구는 이 참조만으로 충족됐다고 가정하지 않는다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: MIT](https://github.com/frappe/frappe/blob/667fbb59e429e45592f02373729188d1c62d2a47/LICENSE)

</details>

<a id="category-7"></a>

## 7. 점검 요청을 세어서 표와 그래프로 보기

가상의 점검 요청 목록에는 요청 번호, 접수일, 설비, 담당자, 상태가 들어 있다고 가정한다. 이 기록을 세어 미처리 비율을 보여 주거나, 설비를 선택했을 때 해당 설비의 수치만 비교하는 화면을 만들 수 있다. 아래 숫자와 화면은 설명용 예시이며, 참고 저장소에 설비 점검 프로그램이 완성되어 있다는 뜻은 아니다.

<a id="f-stats-count-ratio-period"></a>

### 7-1. 전체 요청과 미처리 요청의 건수·비율 계산하기

**예시 상황**

담당자가 현황 화면에서 이번 달 요청 10건을 확인한다. 이 중 미처리가 4건일 때 건수와 비율을 함께 보고 싶은 상황이다.

**동작 예시**

1. 요청 목록에서 이번 달 접수된 기록을 모은다. 각 기록의 상태가 미처리인지 완료인지 구분한다.
2. 전체 10건 중 미처리 4건을 세어 미처리 40%라는 계산 결과를 만든다.
3. 담당자별로도 묶으면 담당자 김민수의 요청 3건 중 미처리 2건처럼 따로 계산할 수 있다.

**참고 코드가 제공하는 부분**

원본에는 같은 값끼리 묶어 건수를 세고 그 묶음 안의 비율을 계산하는 예제가 있다. 날짜를 월 단위로 묶어 평균을 계산하는 예제도 있으며, 이 계산 방법을 점검 요청 자료에 적용할 수 있다. 점검 현황 화면 자체가 들어 있는 것은 아니다.

**따로 만들거나 정할 부분**

요청을 저장한 곳에서 접수일·담당자·상태를 읽어 계산에 넣고, 나온 건수와 비율을 현황 화면에 표시하는 부분을 만들어야 한다. 전체 요청을 기준으로 한 40%와 담당자 자신의 요청을 기준으로 한 비율은 구분해서 이름을 붙인다. 요청이 0건인 달을 어떻게 표시할지도 정한다.

‘오전 10시 당시의 미처리 현황’을 다시 계산한다면 기준 시각·시간대를 입력값으로 고정하고, 이후 생긴 정보뿐 아니라 나중에 바뀐 처리 상태도 섞지 않는다. 당시 상태를 알 수 있는 기록이 필요하다. 현재 현황을 보여주는 경우에는 현재 시각을 사용할 수 있으며, 집계에 사용한 시각을 한 번 정해 계산에 전달하고 화면에도 표시한다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 건수·비율·기간별 집계

- **찾는 말:** 건수 · 비율 · 분모 · 월별 · 기간 비교 · 통계
- **언제 볼까:** 부서·상태별 건수와 비율, 월별 실적을 계산할 때
- **자료 형태:** 라이브러리 함수·사용 예제 — 업무용 검사표·판정 화면은 조합해서 구현
- **저장소·확인 버전:** [pandas-dev/pandas](https://github.com/pandas-dev/pandas) · [`c32acd3c8371`](https://github.com/pandas-dev/pandas/commit/c32acd3c8371a1e33936dea9009d8eef6822ee81)

**먼저 볼 코드**

- [pandas/core/groupby/generic.py](https://github.com/pandas-dev/pandas/blob/c32acd3c8371a1e33936dea9009d8eef6822ee81/pandas/core/groupby/generic.py#L3472-L3600) — `DataFrameGroupBy.value_counts`: 그룹 내부 건수와 normalize=True 비율 예제
- [pandas/core/resample.py](https://github.com/pandas-dev/pandas/blob/c32acd3c8371a1e33936dea9009d8eef6822ee81/pandas/core/resample.py#L1510-L1567) — `Resampler.mean`: DatetimeIndex 데이터를 월별로 묶는 resample('MS') 예제

**참고할 부분과 선정 이유:** value_counts의 normalize 유무로 건수와 그룹 내부 비율을 구분한다. resample 예제는 날짜를 기간으로 묶는 출발점이다. 전월 대비 증감 계산은 집계 결과에 추가할 응용이며 원본 예제는 월별 평균까지 보여준다.

**함께 볼 파일**

- [pandas/core/tools/datetimes.py](https://github.com/pandas-dev/pandas/blob/c32acd3c8371a1e33936dea9009d8eef6822ee81/pandas/core/tools/datetimes.py#L847-L975) — 날짜·시간대 정리
- [pyproject.toml](https://github.com/pandas-dev/pandas/blob/c32acd3c8371a1e33936dea9009d8eef6822ee81/pyproject.toml) — Python·패키지 요구사항

**환경:** Python + pandas. 확인한 개발 커밋의 pyproject.toml은 Python >=3.11. 개발 브랜치 설치를 권하는 자료가 아니며 실전 설치 버전에서 사용할 API를 다시 확인한다.

**한계·별도로 정할 것:** 그룹 내부 비율과 전체 대비 비율의 분모가 다르다. 결측 제외 기본값·0건 기간·0으로 나누기·기간 경계를 정한다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: BSD-3-Clause](https://github.com/pandas-dev/pandas/blob/c32acd3c8371a1e33936dea9009d8eef6822ee81/LICENSE)

</details>

<a id="f-dashboard-chart-details"></a>

### 7-2. 설비를 골라 상세 기록과 그래프 비교하기

**예시 상황**

담당자가 설비 목록 화면에서 A-12와 A-13을 선택해 두 설비의 점검 기록과 측정 수치를 비교하려는 상황이다.

**동작 예시**

1. 설비 목록에서 A-12와 A-13에 해당하는 행을 선택한다.
2. 상세 표에는 선택한 두 설비의 기록만 남고, 비교 그래프도 두 설비의 수치만 보여 준다.
3. A-13의 선택을 해제하면 표와 그래프에서 A-13의 자료가 빠진다.

**참고 코드가 제공하는 부분**

원본 화면 예제에는 표에서 행을 선택하면 선택된 대상의 상세 표와 막대·선 그래프가 바뀌는 동작이 있다. 원본이 만드는 가짜 인물·활동 자료 대신 설비별 자료를 연결하는 방식으로 응용한다.

**따로 만들거나 정할 부분**

실제 요청·측정 기록을 저장한 곳에서 설비 번호와 수치를 읽어 와야 한다. 설비 이름이 바뀌어도 A-12를 같은 설비로 알아보도록 고유 번호를 유지한다. 그래프의 막대를 클릭해 상세 화면으로 이동하는 기능까지 들어 있는 예제는 아니다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 표 선택→상세 표·비교 차트

- **찾는 말:** 현황판 · 드릴다운 · 상세 · 차트 · 선택 · 비교
- **언제 볼까:** 목록에서 특정 대상만 선택해 상세·차트를 비교할 때
- **자료 형태:** 공식 화면 예제 — 실제 데이터 연결은 별도
- **저장소·확인 버전:** [streamlit/docs](https://github.com/streamlit/docs) · [`9cedd224478c`](https://github.com/streamlit/docs/commit/9cedd224478c36e485210be8882d2ac7e8bf188a)

**먼저 볼 코드**

- [python/api-examples-source/tutorials/elements/dataframes/dataframe-row-selections.py](https://github.com/streamlit/docs/blob/9cedd224478c36e485210be8882d2ac7e8bf188a/python/api-examples-source/tutorials/elements/dataframes/dataframe-row-selections.py#L1-L95) — `get_profile_dataset / event.selection.rows / with compare`: 샘플 데이터→행 선택→필터 표→막대·선 차트

**참고할 부분과 선정 이유:** st.dataframe(on_select='rerun'), event.selection.rows, df.iloc[people]과 비교 탭으로 이어지는 코드를 본다. Faker 생성 부분을 실제 데이터 읽기로 바꾸되 이름 대신 안정적인 대상 ID를 유지한다.

**함께 볼 파일**

- [content/develop/tutorials/elements/dataframes/row_selections.md](https://github.com/streamlit/docs/blob/9cedd224478c36e485210be8882d2ac7e8bf188a/content/develop/tutorials/elements/dataframes/row_selections.md#L10-L30) — 설명·튜토리얼 요구 버전

**환경:** Python + Streamlit >=1.49.0(확인한 튜토리얼 기준), pandas, NumPy, Faker. 샘플 사진은 외부 picsum.photos URL 사용.

**한계·별도로 정할 것:** 활동 수치는 난수다. 그래프 클릭 드릴다운이 아니라 표 행 선택에 따라 상세·차트를 바꾸는 예제다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: Apache-2.0](https://github.com/streamlit/docs/blob/9cedd224478c36e485210be8882d2ac7e8bf188a/LICENSE)

</details>

<a id="f-dashboard-metric-selection"></a>

### 7-3. 선택한 설비의 평균을 전체 평균과 비교해서 표시하기

**예시 상황**

관리자가 현황 화면에서 A-12와 A-13을 골랐을 때 두 설비의 평균 온도와 전체 설비 평균의 차이를 큰 숫자로 보고 싶은 상황이다.

**동작 예시**

1. 설비 목록에서 A-12와 A-13을 선택한다. 설명용으로 두 설비의 온도를 각각 60도와 70도라고 가정한다.
2. 선택한 설비의 평균을 65도로 계산한다. 같은 기준으로 계산한 전체 설비 평균이 62도라면 차이는 3도다.
3. 숫자 카드에 선택 설비 평균 65도, 전체 평균보다 3도 높음이라고 표시한다.

**참고 코드가 제공하는 부분**

원본은 선택한 행의 평균과 전체 자료의 평균 차이를 계산해 숫자 카드에 표시한다. 어떤 자료를 선택했는지와 카드의 숫자를 연결하는 부분을 참고한다. 온도 자료나 이 설명의 화면 문구가 원본에 들어 있다는 뜻은 아니다.

**따로 만들거나 정할 부분**

측정 자료에서 같은 단위·같은 기간의 온도 값을 읽어 화면이 사용할 자료로 준비해야 한다. 선택이 없을 때 무엇을 보여 줄지도 정한다. 원본의 보조 숫자는 선택 여부에 따라 의미가 달라지므로 이를 전월 대비 증감이라고 이름 붙이면 안 된다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 선택 데이터에 따른 지표 카드 갱신

- **찾는 말:** 지표 · 카드 · KPI · 평균 · 증감 · 선택 연동
- **언제 볼까:** 선택한 대상 평균을 전체 평균과 비교해 카드로 보여줄 때
- **자료 형태:** 공식 화면 예제 — 실제 데이터 연결은 별도
- **저장소·확인 버전:** [streamlit/docs](https://github.com/streamlit/docs) · [`9cedd224478c`](https://github.com/streamlit/docs/commit/9cedd224478c36e485210be8882d2ac7e8bf188a)

**먼저 볼 코드**

- [python/concept-source/theming-overview-spotify-inspired/data.py](https://github.com/streamlit/docs/blob/9cedd224478c36e485210be8882d2ac7e8bf188a/python/concept-source/theming-overview-spotify-inspired/data.py#L1-L53) — `metric_values / cols[n].metric`: 선택 행 평균·전체 평균과 차이·지표 카드

**참고할 부분과 선정 이유:** metric_values 계산과 cols[n].metric 호출을 참고한다. 카드만 참고하면 테마·다중 페이지 전체를 복사할 필요는 없지만 chart_data 초기화는 필요하다.

**함께 볼 파일**

- [python/concept-source/theming-overview-spotify-inspired/streamlit_app.py](https://github.com/streamlit/docs/blob/9cedd224478c36e485210be8882d2ac7e8bf188a/python/concept-source/theming-overview-spotify-inspired/streamlit_app.py#L1-L24) — session_state.chart_data 초기화

**환경:** Python + Streamlit + pandas + NumPy. data.py는 session_state.chart_data의 a/b/c 열을 전제로 한다. 이 테마 예제의 최소 Streamlit 버전은 별도 미확인.

**한계·별도로 정할 것:** 선택이 없을 때 delta는 표준편차 또는 0이므로 전월 대비 증감으로 오해하지 않는다. data.py 단독 실행 가능 여부는 확인하지 않았다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: Apache-2.0](https://github.com/streamlit/docs/blob/9cedd224478c36e485210be8882d2ac7e8bf188a/LICENSE)

</details>

<a id="category-8"></a>

## 8. 점검 지침을 찾아 답하고 문서 내용을 정리하기

점검 담당자가 지침 문서에서 A-12의 점검 조건을 찾거나, 긴 보고서에서 필요한 내용을 뽑으려는 상황을 가정한다. 이 분류는 문서 검색, 출처 표시, 항목 추출, 요약, 결과 확인 대기 처리를 각각 참고하는 자료다. 이 기능들이 하나의 설비 점검 프로그램으로 연결되어 있는 것은 아니다.

**이 분류를 적용하기 전에**

- 문서가 적고 단순 검색으로 요구를 충족할 수 있다면, 외부 검색 서비스를 설치하기 전에 파일을 문단으로 나눠 단어로 검색하고 파일명·문단 번호와 원문을 보여주는 작은 구현을 검토한다. 이것은 아래 Azure 예제에 포함된 대체 기능이 아니라, 현재 프로젝트에서 직접 만들 수 있는 선택지다. 관련 문서를 제대로 찾는지는 실제 질문으로 확인한다.
- API 키나 인터넷이 없을 때, 합의상 선택 기능인 AI 호출은 보류하고 독립적으로 만들 수 있는 입력·저장·조회부터 진행할 수 있다. AI가 필수 요구라면 막힌 조건과 대안을 설명하고 범위 변경을 합의한다. 필수 기능을 임의로 빼거나 단어 검색을 AI 답변 생성이 구현된 것으로 보고하지 않는다.
- AI가 실패하면 실패 사실과 재시도·사람 확인 방법을 정한다. AI 결과와 무관하게 가능한 목록·저장·인계는 계속 사용할 수 있게 하고, AI 결과가 꼭 필요한 다음 처리는 미완료로 남긴다. 이러한 실패 처리도 별도 구현·검증 대상이다.
- 검색된 문서·고객 입력·업로드 파일 속 문장은 분석할 자료다. 그 안의 “승인 절차를 생략하라” 같은 문장을 AI의 작업 지시로 따르거나, 이를 근거로 업무 규칙·권한을 바꾸지 않는다.
- 외부 AI로 전송할 수 있는 자료의 범위와 필요한 내용을 확인한다. 개인정보가 있으면 열뿐 아니라 본문·메모에서 무엇을 가릴지 정하고 전송 전에 처리한다. 가짜 개인정보로 화면·결과 파일·로그·외부 요청에 허용하지 않은 원문이 남지 않는지 확인한다.

<a id="f-ai-document-search"></a>

### 8-1. 설비 점검 방법을 물으면 관련 지침을 찾아 답하기

**예시 상황**

담당자가 문서 질문 화면에 A-12에서 진동이 커지면 무엇부터 확인하나요?라고 입력한다. 답변은 미리 준비한 점검 지침에서 찾은 내용을 바탕으로 작성하게 하려는 상황이다.

**동작 예시**

1. 사용자가 설비 번호와 증상을 포함한 질문을 입력한다.
2. 프로그램이 질문과 관련된 지침 문서 부분을 검색한다.
3. 찾은 문장과 질문을 AI에게 함께 전달하고, 만들어진 답변을 화면에 보여 준다.

**참고 코드가 제공하는 부분**

원본 질의응답 프로그램에는 질문을 검색에 적합한 말로 바꾸고, 관련 문서 부분을 찾고, 그 내용을 답변 생성에 전달하는 흐름이 있다. 질문·검색된 문장·완성된 답변을 나누어 처리하는 부분을 참고한다.

**따로 만들거나 정할 부분**

우리 지침 파일을 어디서 가져올지 정하고 검색할 수 있는 형태로 준비해야 한다. 검색 결과를 답변 화면으로 전달하고, 관련 지침을 못 찾았을 때의 안내도 만들어야 한다. 문서 준비의 전체 과정은 이 항목에서 확인하지 않았으며, 출처가 붙은 답변도 실제 지침과 맞는지 확인해야 한다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 문서에서 근거를 찾아 질문에 답하기

- **찾는 말:** 문서 검색 · RAG · 질의응답 · 검색어 변환 · 벡터 검색 · 사내 문서
- **언제 볼까:** 준비한 문서들에서 질문과 관련 있는 부분을 찾아 답변에 함께 넣을 때
- **자료 형태:** 문서 질의응답 앱의 일부 — 검색 서비스·인덱스가 필요
- **저장소·확인 버전:** [Azure-Samples/azure-search-openai-demo](https://github.com/Azure-Samples/azure-search-openai-demo) · [`558ffd397edd`](https://github.com/Azure-Samples/azure-search-openai-demo/commit/558ffd397eddcfe4da5c85ebc285796b367eb9b2)

**먼저 볼 코드**

- [app/backend/approaches/chatreadretrieveread.py](https://github.com/Azure-Samples/azure-search-openai-demo/blob/558ffd397eddcfe4da5c85ebc285796b367eb9b2/app/backend/approaches/chatreadretrieveread.py) — `ChatReadRetrieveReadApproach.run_search_approach / run_until_final_call`: 대화에서 검색어를 만들고 검색 결과를 모은 뒤, 근거와 질문을 답변 생성에 전달한다.
- [app/backend/approaches/approach.py](https://github.com/Azure-Samples/azure-search-openai-demo/blob/558ffd397eddcfe4da5c85ebc285796b367eb9b2/app/backend/approaches/approach.py) — `Approach.search`: 텍스트·벡터 검색, 필터, 검색 개수, 점수 조건을 처리한다.

**참고할 부분과 선정 이유:** ‘질문을 검색어로 바꾸기 → 관련 문서 검색 → 찾은 내용과 출처를 답변 생성에 전달’하는 연결을 참고한다. 검색어·문서 내용·생성된 답변을 구분해 두면 어떤 단계에서 잘못됐는지 확인하기 쉽다. 이 사례는 Azure 검색 서비스를 사용하므로 다른 검색 도구에 그대로 연결되는 코드는 아니다.

**함께 볼 파일**

- [app/backend/approaches/prompts/chat_answer.system.jinja2](https://github.com/Azure-Samples/azure-search-openai-demo/blob/558ffd397eddcfe4da5c85ebc285796b367eb9b2/app/backend/approaches/prompts/chat_answer.system.jinja2) — 검색된 내용과 출처를 답변에 쓰도록 안내하는 템플릿
- [app/backend/requirements.in](https://github.com/Azure-Samples/azure-search-openai-demo/blob/558ffd397eddcfe4da5c85ebc285796b367eb9b2/app/backend/requirements.in) — 서버의 주요 의존성

**환경:** Python·Quart·OpenAI SDK·Azure AI Search를 쓰는 서버와 React·TypeScript 화면. requirements.in에 검색 서비스·인증·템플릿 관련 의존성이 있다. 검색 인덱스와 사용 권한, API 설정이 필요하다. 다른 기술을 쓰는 과제에서는 처리 순서와 데이터 연결 방법을 참고한다.

**한계·별도로 정할 것:** 문서 수집·색인 생성 전체 과정은 이 항목에서 확인한 범위 밖이다. 검색이 되거나 출처가 붙어도 답이 정확하다는 보장은 없다. 문서별 접근 권한, 근거 없음 처리, 검색·답변 품질은 실제 과제에서 확인해야 한다. 규정·지침을 다룬다면 문서 버전·효력일·원문 보관본을 어떻게 표시할지, 서로 다른 문서의 답이 충돌할 때 무엇을 우선하거나 보류할지는 합의로 정한다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: MIT](https://github.com/Azure-Samples/azure-search-openai-demo/blob/558ffd397eddcfe4da5c85ebc285796b367eb9b2/LICENSE)

</details>

<a id="f-ai-citations"></a>

### 8-2. AI 답변에서 근거로 쓴 지침 원문 열어 보기

**예시 상황**

담당자가 AI 답변을 읽다가 정말 지침에 적힌 내용인지 확인하려는 상황이다. 답변 옆의 출처 번호를 누르면 해당 지침 문서를 열 수 있게 한다.

**동작 예시**

1. 검색 결과로 전달받은 문서 목록과 AI 답변에 표시된 출처를 맞춘다.
2. 같은 지침 문서가 답변에서 여러 번 언급되면 같은 번호로 정리해 표시한다.
3. 사용자가 출처 번호를 누르면 그 번호에 연결된 원문을 확인한다.

**참고 코드가 제공하는 부분**

원본에는 답변의 출처 표시를 실제로 전달받은 문서 목록과 대조해 번호와 링크를 만드는 부분이 있다. 같은 출처를 반복해서 별개 항목으로 만드는 것을 줄이는 방법도 참고한다.

**따로 만들거나 정할 부분**

지침을 저장한 곳의 주소나 파일 위치를 검색 결과와 함께 전달해야 한다. 링크를 누른 사람이 그 지침을 읽어도 되는지도 확인해야 한다. 이 처리는 링크를 만드는 것이며, 지침 내용이 AI의 설명을 실제로 뒷받침하는지 판정하는 기능은 아니다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 답변에 출처 링크 붙이기·같은 출처 정리

- **찾는 말:** 출처 · 인용 · 근거 링크 · citation · 답변 검토
- **언제 볼까:** AI 답변을 읽는 사람이 어떤 문서를 근거로 썼는지 열어볼 수 있게 할 때
- **자료 형태:** 문서 질의응답 앱의 일부 — 검색 서비스·인덱스가 필요
- **저장소·확인 버전:** [Azure-Samples/azure-search-openai-demo](https://github.com/Azure-Samples/azure-search-openai-demo) · [`558ffd397edd`](https://github.com/Azure-Samples/azure-search-openai-demo/commit/558ffd397eddcfe4da5c85ebc285796b367eb9b2)

**먼저 볼 코드**

- [app/frontend/src/components/Answer/AnswerParser.tsx](https://github.com/Azure-Samples/azure-search-openai-demo/blob/558ffd397eddcfe4da5c85ebc285796b367eb9b2/app/frontend/src/components/Answer/AnswerParser.tsx) — `collectCitations / renderCitation / parseAnswerToHtml / extractCitationDetails`: 답변의 출처 표시를 서버가 준 출처 목록과 맞추고, 같은 출처를 묶어 번호와 링크를 만든다.

**참고할 부분과 선정 이유:** 출처 문자열을 모두 링크로 만드는 대신 answer.context.data_points.citations의 항목과 대조하는 부분을 참고한다. collectCitations가 중복 출처를 정리하고 renderCitation이 화면 링크를 만든다. 스트리밍 중 아직 완성되지 않은 출처 표시는 별도로 처리한다.

**함께 볼 파일**

- [app/backend/approaches/chatreadretrieveread.py](https://github.com/Azure-Samples/azure-search-openai-demo/blob/558ffd397eddcfe4da5c85ebc285796b367eb9b2/app/backend/approaches/chatreadretrieveread.py) — 답변과 함께 검색 결과·출처 정보를 제공하는 서버 흐름
- [app/backend/approaches/prompts/chat_answer.system.jinja2](https://github.com/Azure-Samples/azure-search-openai-demo/blob/558ffd397eddcfe4da5c85ebc285796b367eb9b2/app/backend/approaches/prompts/chat_answer.system.jinja2) — 답변의 출처 표기 형식을 정하는 템플릿

**환경:** Python·Quart·OpenAI SDK·Azure AI Search를 쓰는 서버와 React·TypeScript 화면. requirements.in에 검색 서비스·인증·템플릿 관련 의존성이 있다. 검색 인덱스와 사용 권한, API 설정이 필요하다. 다른 기술을 쓰는 과제에서는 처리 순서와 데이터 연결 방법을 참고한다.

**한계·별도로 정할 것:** 출처 링크의 존재를 확인하는 화면 처리다. 해당 문서가 실제로 주장 내용을 뒷받침하는지 판정하지는 않는다. 원문 열람 권한과 화면에서 안전하게 표시하는 방법도 별도로 확인한다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: MIT](https://github.com/Azure-Samples/azure-search-openai-demo/blob/558ffd397eddcfe4da5c85ebc285796b367eb9b2/LICENSE)

</details>

<a id="f-ai-structured-fields"></a>

### 8-3. 자유롭게 쓴 점검 요청을 설비·증상·담당자 칸으로 나누기

**예시 상황**

요청자가 A-12에서 소음이 커졌고 담당자는 김민수입니다라고 적었다. 이를 설비 번호, 증상, 담당자 칸으로 나누어 담당자가 확인하게 하려는 상황이다.

**동작 예시**

1. AI에게 나눌 항목을 설비 번호·증상·담당자로 미리 알려 준다.
2. 요청 문장을 전달하면 각 항목에 대응하는 값을 받아온다.
3. 설비 번호 A-12, 증상 소음 증가, 담당자 김민수처럼 나눈 결과를 확인한다. 이는 설명용 기대 결과이며 실제 추출 성공을 보장하지 않는다.

**참고 코드가 제공하는 부분**

원본에는 문서에서 연도·이름·요약 등을 정해진 항목에 맞춰 받는 예제와, 미리 정한 분류 중에서 값을 받는 예제가 있다. 받을 항목과 허용할 분류를 먼저 정하는 방법을 점검 요청에 응용한다.

**따로 만들거나 정할 부분**

요청 입력칸의 문장을 AI에게 보내고 반환된 값을 확인 화면에 채우는 부분을 만들어야 한다. 담당자가 확인한 값을 요청 R-001에 저장할지, 초안으로만 둘지도 정한다. 원문에 담당자가 없을 때 추측한 이름을 저장하지 않도록 모름·누락 처리와 원문 대조가 필요하다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 문장에서 정해진 항목 추출·허용된 분류로 받기

- **찾는 말:** 정보 추출 · 정형 출력 · JSON · 분류 · Enum · 문서 필드
- **언제 볼까:** 자유로운 문장을 연도·이름·요약 같은 항목이나 정해진 분류 값으로 바꾸고 싶을 때
- **자료 형태:** 공식 노트북 코드 예제 — 입력·오류·API 환경을 과제에 맞춰 보완
- **저장소·확인 버전:** [openai/openai-cookbook](https://github.com/openai/openai-cookbook) · [`a8132ca2f7a5`](https://github.com/openai/openai-cookbook/commit/a8132ca2f7a5de3a6cf15d9e79d172787b42b697)

**먼저 볼 코드**

- [examples/Structured_Outputs_Intro.ipynb](https://github.com/openai/openai-cookbook/blob/a8132ca2f7a5de3a6cf15d9e79d172787b42b697/examples/Structured_Outputs_Intro.ipynb) — `ArticleSummary / get_article_summary / Category / ProductSearchParameters / get_response`: 필드 이름과 자료형을 선언하고 파싱된 결과를 받는 예제, 선택 가능한 분류를 Enum으로 제한하는 예제

**참고할 부분과 선정 이유:** ArticleSummary는 추출 결과의 모양을 먼저 선언한다. get_article_summary는 그 형식으로 응답을 받는다. Category와 ProductSearchParameters는 허용된 분류 값으로 검색 인자를 구성하는 예제다. 실제 과제의 필드와 ‘알 수 없음’ 처리 정책으로 바꿔야 한다.

**함께 볼 파일**

- [examples/Structured_Outputs_Intro.ipynb](https://github.com/openai/openai-cookbook/blob/a8132ca2f7a5de3a6cf15d9e79d172787b42b697/examples/Structured_Outputs_Intro.ipynb) — 같은 노트북의 모델 설정·Pydantic import·openai.pydantic_function_tool·응답 확인 코드

**환경:** Python·OpenAI SDK·Pydantic 또는 tiktoken을 쓰는 노트북 예제. 예제에 적힌 모델 이름과 API 호출 방식은 작성 당시의 것이므로 실제 사용 가능 여부와 설치할 SDK에서의 문법을 구현 시 확인한다. API 이용 비용과 실행 결과는 확인하지 않았다.

**한계·별도로 정할 것:** 형식에 맞는 값이 사실이라는 뜻은 아니다. 원문 대조, 필수값 누락, 거절 응답, 오류 처리를 별도로 만든다. 이 예제에 실제 상품 검색 DB가 구현되어 있다는 뜻도 아니다. 모델 이름과 SDK 호출 방식은 현재 환경에서 다시 확인한다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: MIT](https://github.com/openai/openai-cookbook/blob/a8132ca2f7a5de3a6cf15d9e79d172787b42b697/LICENSE)

</details>

<a id="f-ai-long-summary"></a>

### 8-4. 긴 점검 보고서를 나누어 요약한 뒤 모으기

**예시 상황**

담당자가 여러 페이지짜리 점검 보고서에서 전체 내용을 짧게 확인하고 싶은 상황이다. 문서가 길어서 한 번에 요약하기 어렵다고 가정한다.

**동작 예시**

1. 보고서의 글을 읽어 여러 부분으로 나눈다.
2. 각 부분을 AI에게 보내 요약을 받고, 필요하면 앞부분의 요약을 다음 부분의 참고 내용으로 전달한다.
3. 부분별 요약을 모아 하나의 결과로 보여 준다.

**참고 코드가 제공하는 부분**

원본에는 글의 길이와 구분자를 기준으로 나누고, 부분별 요약을 생성해 합치는 예제가 있다. 얼마나 자세히 요약할지에 따라 나누는 개수를 조절하는 부분을 참고한다.

**따로 만들거나 정할 부분**

보고서 파일에서 글을 읽어 요약 처리에 넣고, 나온 요약을 화면이나 결과 파일에 담는 부분을 연결해야 한다. 원본은 너무 긴 한 덩어리를 건너뛸 수 있으므로 모든 원문을 다뤄야 한다면 이 부분을 고쳐야 한다. 빠진 중요 내용과 반복 요청에 따른 비용도 확인한다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 긴 문서를 나눠 요약하기

- **찾는 말:** 긴 문서 · 요약 · 분할 · 토큰 · 회의록 · 보고서
- **언제 볼까:** 긴 문서를 여러 부분으로 나눠 부분 요약을 만들고 합치려 할 때
- **자료 형태:** 공식 노트북 코드 예제 — 입력·오류·API 환경을 과제에 맞춰 보완
- **저장소·확인 버전:** [openai/openai-cookbook](https://github.com/openai/openai-cookbook) · [`a8132ca2f7a5`](https://github.com/openai/openai-cookbook/commit/a8132ca2f7a5de3a6cf15d9e79d172787b42b697)

**먼저 볼 코드**

- [examples/Summarizing_long_documents.ipynb](https://github.com/openai/openai-cookbook/blob/a8132ca2f7a5de3a6cf15d9e79d172787b42b697/examples/Summarizing_long_documents.ipynb) — `tokenize / chunk_on_delimiter / combine_chunks_with_no_minimum / summarize`: 토큰 수와 구분자로 문서를 나누고 부분별 요약을 생성해 합친다.

**참고할 부분과 선정 이유:** summarize의 detail이 문서 분할 개수에 영향을 주고, summarize_recursively는 이전 요약을 다음 부분의 문맥으로 전달할지 정한다. 문서 분할·부분 요약·합치기를 서로 구분한 구조를 참고한다.

**함께 볼 파일**

- [examples/Summarizing_long_documents.ipynb](https://github.com/openai/openai-cookbook/blob/a8132ca2f7a5de3a6cf15d9e79d172787b42b697/examples/Summarizing_long_documents.ipynb) — 같은 노트북의 get_chat_completion, tiktoken·tqdm import 및 예제 호출

**환경:** Python·OpenAI SDK·Pydantic 또는 tiktoken을 쓰는 노트북 예제. 예제에 적힌 모델 이름과 API 호출 방식은 작성 당시의 것이므로 실제 사용 가능 여부와 설치할 SDK에서의 문법을 구현 시 확인한다. API 이용 비용과 실행 결과는 확인하지 않았다.

**한계·별도로 정할 것:** 너무 긴 한 덩어리는 combine_chunks_with_no_minimum에서 건너뛸 수 있다. 원문 누락이 허용되지 않으면 이 동작을 그대로 쓰면 안 된다. 빈 입력, 구분자 없는 긴 입력, 요약의 정보 손실, 호출 횟수·비용을 별도로 검증한다. 예제 모델의 현재 사용 가능 여부는 미확인.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: MIT](https://github.com/openai/openai-cookbook/blob/a8132ca2f7a5de3a6cf15d9e79d172787b42b697/LICENSE)

</details>

<a id="f-ai-review-boundary"></a>

### 8-5. AI가 읽은 송장 금액을 재계산하고 확인 대기로 두기

**예시 상황**

이 항목은 점검 업무로 바로 바꿔 설명하지 않고 원본의 송장을 예로 든다. AI가 읽은 송장의 수량·단가·배송비·총액을 사람이 확정하기 전에 계산으로 확인하려는 상황이다.

**동작 예시**

1. 설명용으로 AI 결과가 수량 2개, 단가 1만 원, 배송비 3천 원, 총액 2만 3천 원이라고 가정한다.
2. 프로그램이 2×1만 원+3천 원을 다시 계산해 2만 3천 원을 얻는다. AI가 적은 계산 결과가 이 값과 같고, 송장에 적힌 총액과의 차이도 맞게 계산했는지 확인한다.
3. 다른 예로 송장 총액은 2만 5천 원인데 재계산한 합계는 2만 3천 원이라고 가정한다. 다른 필수 항목이 올바르고 AI가 차이를 2천 원으로 정확히 적었다면 계산 검사는 통과한다. 이는 차이를 정확히 계산했다는 뜻이지, 송장 금액이 맞거나 승인됐다는 뜻은 아니다.
4. 필수 항목과 계산 검사를 통과한 결과도 최종 확정하지 않고 사람 확인 대기로 표시한다. 금액 차이를 별도 문구로 보여주는 화면은 우리가 추가로 만드는 부분이다.

**참고 코드가 제공하는 부분**

원본에는 송장 금액의 계산과 필수 항목을 검사하고 결과에 확인 대기 상태를 붙이는 부분이 있다. 계산으로 검사할 수 있는 내용과 사람이 봐야 하는 내용을 구분한다는 점을 참고한다.

**따로 만들거나 정할 부분**

송장 총액과 재계산한 합계가 달라도, 그 차이를 AI가 정확히 계산했다면 확인 대기로 넘길 수 있다. 또한 계산이 맞아도 AI가 원문 숫자를 잘못 읽었을 수 있다. 사람이 원문과 추출 결과를 보고 수정·승인할 화면과 최종 결과 저장은 별도로 만들어야 한다. 이를 점검 업무에 응용한다면 점검값 중 무엇을 계산으로 검사할 수 있는지 먼저 정해야 하며, 원본에 점검 판정 기능이 있는 것은 아니다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** AI 결과를 코드로 검사하고 사람 확인 대기로 넘기기

- **찾는 말:** AI 검증 · 사람 확인 · 승인 대기 · 계산 검증 · human review
- **언제 볼까:** AI가 추출한 금액·판정을 그대로 확정하지 않고 검사한 뒤 사람이 확인하게 할 때
- **자료 형태:** 에이전트 앱의 결과 검증 부분 — 사람의 수정·승인 화면은 별도
- **저장소·확인 버전:** [openai/openai-cookbook](https://github.com/openai/openai-cookbook) · [`a8132ca2f7a5`](https://github.com/openai/openai-cookbook/commit/a8132ca2f7a5de3a6cf15d9e79d172787b42b697)

**먼저 볼 코드**

- [examples/agents_api/apps/document_review/agent.py](https://github.com/openai/openai-cookbook/blob/a8132ca2f7a5de3a6cf15d9e79d172787b42b697/examples/agents_api/apps/document_review/agent.py) — `validate_review / 보고서 수집 후 awaiting_approval 지정 부분`: 필수 항목·허용 판정값·유한한 금액·송장 산술을 검사하고 결과를 확인 대기로 표시한다.

**참고할 부분과 선정 이유:** validate_review는 송장의 수량×단가 합계와 배송비, 총액 차이를 Decimal로 다시 확인한다. 보고서 수집 부분은 검사를 통과한 결과에도 awaiting_approval 상태를 붙인다. ‘AI 초안 → 코드로 확인 가능한 값 검사 → 사람 확인 대기’라는 경계를 참고한다.

**함께 볼 파일**

- [examples/agents_api/apps/document_review/main.py](https://github.com/openai/openai-cookbook/blob/a8132ca2f7a5de3a6cf15d9e79d172787b42b697/examples/agents_api/apps/document_review/main.py) — 앱 시작점과 Python·패키지 요구사항
- [examples/agents_api/apps/document_review/sandbox.py](https://github.com/openai/openai-cookbook/blob/a8132ca2f7a5de3a6cf15d9e79d172787b42b697/examples/agents_api/apps/document_review/sandbox.py) — 문서·결과 경로와 실행 컨테이너가 연결되는 방식

**환경:** 원본 앱은 Python >=3.14·openai>=3.13.0·Docker 등을 선언한다(main.py 기준). 여기서는 결과 검증과 확인 대기 상태 전환 부분만 참고한다. 전체 에이전트 앱의 설치·지원 환경·운영 가능 여부는 미검증.

**한계·별도로 정할 것:** 원문에서 올바른 숫자를 추출했는지까지 증명하지 않는다. 계약서에는 송장과 같은 산술 검사를 하지 않는다. 확인한 코드에 사람이 값을 고치고 최종 승인하는 화면까지 구현되어 있다는 뜻은 아니다. 그런 화면은 입력·수정 및 승인 항목을 조합해 별도로 설계한다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: MIT](https://github.com/openai/openai-cookbook/blob/a8132ca2f7a5de3a6cf15d9e79d172787b42b697/LICENSE)

</details>

**아직 준비되지 않은 부분**

- 점검 지침 원문과 AI 답을 나란히 띄우고, 담당자가 값을 고친 뒤 최종 확정하는 완성 화면은 확인하지 않았다. 그러한 화면이 필요하면 문서 표시·입력 수정·확정 기록을 함께 만들어야 한다.

<a id="category-9"></a>

## 9. 설비를 점검할 시간을 보고 예약하기

A-12를 언제 점검할지 정하고, 같은 시간에 다른 점검이 잡혀 있는지 확인하는 프로그램을 가정한다. 달력 표시, 빈 시간 계산, 예약 변경, 겹침 경고는 서로 다른 처리다. 참고 원본은 일반 예약 프로그램이므로 설비·공간의 점검 예약에 맞춰 바꾸어야 한다.

<a id="f-9-1"></a>

### 9-1. 점검 일정을 달력에서 보고 시간 옮기기

**예시 상황**

담당자가 달력 화면에서 A-12의 수요일 오전 10시 점검을 보고, 시작 시간을 오전 11시로 바꾸려는 상황이다.

**동작 예시**

1. 달력에서 이번 주를 열면 해당 기간의 예약이 시작·종료 시간에 맞춰 표시된다.
2. A-12 점검을 오전 11시 위치로 끌어 놓으면 바뀐 시간을 저장하도록 요청한다.
3. 저장이 실패하면 달력의 예약을 원래 위치로 되돌린다.

**참고 코드가 제공하는 부분**

원본에는 예약 기록을 달력에 표시하고, 일·주·월 보기와 끌어서 시간 바꾸기를 연결하는 처리가 있다. 현재 달력에 보이는 기간의 예약만 가져와 표시하는 방법도 참고한다.

**따로 만들거나 정할 부분**

설비 번호·점검 제목·시작·종료 시간을 예약 저장소에서 읽어 달력에 전달해야 한다. 이동한 시간을 다시 예약에 저장하는 처리도 연결한다. 달력의 빈칸은 화면 표시일 뿐이므로 실제 예약 가능한지와 다른 예약과 겹치는지는 따로 검사한다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 달력 표시·기간별 일정 조회·드래그 변경

- **찾는 말:** 달력 · 캘린더 · 일정 · 일간 · 주간 · 월간 · 드래그
- **언제 볼까:** 예약이나 작업 일정을 날짜별로 보여주고 담당자·서비스 조건으로 바꿔 볼 때.
- **자료 형태:** 예약 애플리케이션 구현 — 화면·서버·DB가 연결된 예제
- **저장소·확인 버전:** [alextselegidis/easyappointments](https://github.com/alextselegidis/easyappointments) · [`f6c8a4c2f364`](https://github.com/alextselegidis/easyappointments/commit/f6c8a4c2f364bf8c64b1f913a531a7134dcfd3c6)

**먼저 볼 코드**

- [assets/js/utils/calendar_default_view.js](https://github.com/alextselegidis/easyappointments/blob/f6c8a4c2f364bf8c64b1f913a531a7134dcfd3c6/assets/js/utils/calendar_default_view.js#L863-L933) — `refreshCalendarAppointments / createAppointmentEvents`: 현재 달력 범위의 예약을 조회하고 API 응답을 달력 이벤트로 변환한다.
- [assets/js/utils/calendar_default_view.js](https://github.com/alextselegidis/easyappointments/blob/f6c8a4c2f364bf8c64b1f913a531a7134dcfd3c6/assets/js/utils/calendar_default_view.js#L1307-L1360) — `initialize / onEventDrop / onEventResize`: 달력 보기와 선택·이동·길이 변경 이벤트를 연결한다.
- [application/controllers/Calendar.php](https://github.com/alextselegidis/easyappointments/blob/f6c8a4c2f364bf8c64b1f913a531a7134dcfd3c6/application/controllers/Calendar.php#L862-L1048) — `get_calendar_appointments`: 화면의 조회 기간과 선택 조건에 맞는 예약 데이터를 반환한다.

**참고할 부분과 선정 이유:** 먼저 createAppointmentEvents에서 예약의 ID·시작·종료·제목을 달력이 받는 필드로 매핑하는 부분을 참고한다. refreshCalendarAppointments는 화면에 보이는 시작일/종료일만 서버에 요청한 뒤 기존 이벤트를 교체한다. initialize는 일/주/월 보기와 eventDrop/eventResize/select를 연결한다. 드래그 저장에는 실패 시 원래 위치로 되돌리는 처리를 함께 따라 읽는다.

**함께 볼 파일**

- [assets/js/http/calendar_http_client.js](https://github.com/alextselegidis/easyappointments/blob/f6c8a4c2f364bf8c64b1f913a531a7134dcfd3c6/assets/js/http/calendar_http_client.js) — 조회·저장 API 요청과 CSRF 토큰, 충돌 응답 처리
- [assets/js/pages/calendar.js](https://github.com/alextselegidis/easyappointments/blob/f6c8a4c2f364bf8c64b1f913a531a7134dcfd3c6/assets/js/pages/calendar.js) — 달력 페이지 시작과 기본/표 보기 선택
- [package.json](https://github.com/alextselegidis/easyappointments/blob/f6c8a4c2f364bf8c64b1f913a531a7134dcfd3c6/package.json) — FullCalendar·jQuery·Moment 등 화면 의존성

**환경:** Easy!Appointments composer.json 표기 1.6.1. PHP >=8.2·MySQL·CodeIgniter 방식 서버, 화면은 jQuery·FullCalendar ^6.1.19·Moment. composer.json/package.json/config-sample.php를 함께 확인.

**한계·별도로 정할 것:** 달력에서 빈칸으로 보인다는 사실은 서버의 예약 가능 판정이나 중복 예약 차단을 의미하지 않는다. 기존 코드의 고객·제공자·서비스 필드를 과제의 사람·설비·공간에 맞게 바꿔야 한다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: GPL-3.0](https://github.com/alextselegidis/easyappointments/blob/f6c8a4c2f364bf8c64b1f913a531a7134dcfd3c6/LICENSE)

</details>

<a id="f-9-2"></a>

### 9-2. 근무시간과 기존 예약을 빼고 점검 가능한 시간 찾기

**예시 상황**

담당자가 A-12의 1시간 점검을 예약하려 한다. 설명용으로 운영시간은 오전 9시~오후 6시, 점심은 12~13시, 기존 점검은 10~11시라고 가정한다.

**동작 예시**

1. 예약 날짜와 필요한 점검 시간 1시간을 선택한다.
2. 프로그램이 운영시간에서 점심시간과 기존 예약 시간을 제외한다.
3. 예약 시작 간격을 1시간으로 정했다면 오전 9시나 11시처럼 1시간이 비는 시작 시각을 후보로 보여 준다.

**참고 코드가 제공하는 부분**

원본에는 운영시간·휴식·기존 예약을 이용해 빈 시간대를 구하고, 필요한 시간 길이와 정원을 고려해 예약 후보를 만드는 처리가 있다. 변경 중인 예약을 자기 자신과 겹친다고 잘못 판단하지 않게 제외하는 부분도 참고한다.

**따로 만들거나 정할 부분**

설비별 이용 가능 시간, 점검 소요시간, 기존 예약을 어디에 저장할지 정하고 이 계산에 전달해야 한다. 보여 준 후보는 조회 당시의 빈 시간이며 선택한 사람을 위해 확보된 시간이 아니다. 최종 저장 시 다른 예약이 생겼는지 다시 확인해야 한다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 예약 가능한 시간 계산

- **찾는 말:** 빈 시간 · 예약 가능 · 근무시간 · 휴식 · 휴무 · 정원 · 예약 간격
- **언제 볼까:** 운영시간·휴식·기존 예약·서비스 소요시간을 고려해 선택 가능한 시간을 제공할 때.
- **자료 형태:** 예약 애플리케이션 구현 — 화면·서버·DB가 연결된 예제
- **저장소·확인 버전:** [alextselegidis/easyappointments](https://github.com/alextselegidis/easyappointments) · [`f6c8a4c2f364`](https://github.com/alextselegidis/easyappointments/commit/f6c8a4c2f364bf8c64b1f913a531a7134dcfd3c6)

**먼저 볼 코드**

- [application/libraries/Availability.php](https://github.com/alextselegidis/easyappointments/blob/f6c8a4c2f364bf8c64b1f913a531a7134dcfd3c6/application/libraries/Availability.php#L61-L192) — `get_available_hours / get_available_periods / generate_available_hours / consider_multiple_attendants`: 운영시간에서 점유·차단 시간을 제외하고 소요시간과 간격으로 예약 후보를 만든다.
- [application/controllers/Booking.php](https://github.com/alextselegidis/easyappointments/blob/f6c8a4c2f364bf8c64b1f913a531a7134dcfd3c6/application/controllers/Booking.php#L622-L663) — `get_available_hours / check_datetime_availability`: 조회 응답 및 저장 전 재확인에서 Availability를 호출한다.

**참고할 부분과 선정 이유:** get_available_hours를 시작점으로 읽는다. 서비스 정원이 1보다 크면 consider_multiple_attendants로 슬롯별 예약 인원을 비교하고, 아니면 빈 기간을 계산한 뒤 generate_available_hours로 시작 시각 후보를 만든다. 운영시간 예외·휴식·차단 기간·기존 예약과 신규 예약의 소요시간을 각각 입력으로 다루는 방식을 참고한다. 변경 중인 예약 ID를 제외해 자기 자신과 충돌하지 않게 하는 흐름도 포함한다.

**함께 볼 파일**

- [application/models/Appointments_model.php](https://github.com/alextselegidis/easyappointments/blob/f6c8a4c2f364bf8c64b1f913a531a7134dcfd3c6/application/models/Appointments_model.php) — 특정 시간 구간의 기존 예약 인원 조회와 종료 시각 계산
- [application/controllers/Booking.php](https://github.com/alextselegidis/easyappointments/blob/f6c8a4c2f364bf8c64b1f913a531a7134dcfd3c6/application/controllers/Booking.php) — 서비스·제공자 선택, 후보 조회, 등록 전 재확인
- [composer.json](https://github.com/alextselegidis/easyappointments/blob/f6c8a4c2f364bf8c64b1f913a531a7134dcfd3c6/composer.json) — PHP 요구 버전·서버 의존성

**환경:** Easy!Appointments composer.json 표기 1.6.1. PHP >=8.2·MySQL·CodeIgniter 방식 서버, 화면은 jQuery·FullCalendar ^6.1.19·Moment. composer.json/package.json/config-sample.php를 함께 확인.

**한계·별도로 정할 것:** 결과는 조회 당시 후보 시간이다. 표시 이후 다른 사용자가 예약할 수 있으므로 이를 예약 확정이나 잠금으로 취급하지 않는다. 시간대·일광절약시간 경계는 해당 과제에서 별도 검증해야 한다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: GPL-3.0](https://github.com/alextselegidis/easyappointments/blob/f6c8a4c2f364bf8c64b1f913a531a7134dcfd3c6/LICENSE)

</details>

<a id="f-9-3"></a>

### 9-3. 점검 예약을 만들고 시간을 바꾸거나 취소하기

**예시 상황**

담당자가 요청 R-001에 대해 A-12의 점검 예약을 만들고, 나중에 시간을 바꾸거나 점검 불필요로 취소하려는 상황이다.

**동작 예시**

1. 날짜·시작·종료 시간을 입력해 새 예약을 저장한다.
2. 기존 예약을 다시 열어 시간을 변경할 때는 새 예약을 하나 더 만드는 대신 그 예약을 수정한다.
3. 취소할 때는 어느 예약인지와 변경할 권한을 확인하고 취소 처리를 한다.

**참고 코드가 제공하는 부분**

원본은 새 예약과 변경 요청을 구분하고, 변경할 예약을 확인한 뒤 저장한다. 취소 대상 확인과 삭제 후 알림을 처리하는 흐름도 있다. 요청 R-001과의 연결은 원본 기능이 아니라 점검 프로그램에 적용할 때 추가할 관계다.

**따로 만들거나 정할 부분**

예약에 요청 번호 R-001과 설비 A-12를 연결해 저장하고, 변경·취소 화면에서 같은 예약을 찾아야 한다. 원본 취소는 실제 기록을 삭제하므로 취소 사유와 이력을 남기고 싶다면 삭제 대신 취소 상태와 사유를 보존하도록 바꿔야 한다. 예약 변경에 쓰이는 비밀 식별 정보도 공개하면 안 된다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 예약 등록·변경·취소

- **찾는 말:** 예약 등록 · 예약 변경 · 시간 변경 · 예약 취소 · 취소 사유
- **언제 볼까:** 사용자가 예약을 만들고 기존 예약의 시간·내용을 바꾸거나 취소할 때.
- **자료 형태:** 예약 애플리케이션 구현 — 화면·서버·DB가 연결된 예제
- **저장소·확인 버전:** [alextselegidis/easyappointments](https://github.com/alextselegidis/easyappointments) · [`f6c8a4c2f364`](https://github.com/alextselegidis/easyappointments/commit/f6c8a4c2f364bf8c64b1f913a531a7134dcfd3c6)

**먼저 볼 코드**

- [application/controllers/Booking.php](https://github.com/alextselegidis/easyappointments/blob/f6c8a4c2f364bf8c64b1f913a531a7134dcfd3c6/application/controllers/Booking.php#L355-L605) — `register`: 신규/변경 모드를 구분하고 변경 시 예약 ID와 hash의 일치를 검사한 뒤 저장한다.
- [application/models/Appointments_model.php](https://github.com/alextselegidis/easyappointments/blob/f6c8a4c2f364bf8c64b1f913a531a7134dcfd3c6/application/models/Appointments_model.php) — `save / validate / insert / update / delete`: 입력 검증과 신규 삽입·수정·삭제의 DB 처리 경로.
- [application/controllers/Booking_cancellation.php](https://github.com/alextselegidis/easyappointments/blob/f6c8a4c2f364bf8c64b1f913a531a7134dcfd3c6/application/controllers/Booking_cancellation.php#L49-L168) — `of`: POST·예약 hash·취소 사유를 확인하고 예약을 삭제한 뒤 알림/연동을 처리한다.

**참고할 부분과 선정 이유:** register에서 신규 요청의 임의 ID를 제거하고, 변경 요청에서는 기존 ID와 예약 hash가 함께 맞는지 검증하는 부분을 먼저 참고한다. 모델 save는 ID 유무로 insert/update를 나눈다. 취소는 Booking_cancellation.of의 조회→대상 식별→삭제→알림 순서를 참고한다. 내부 관리자 화면은 Calendar.save_appointment/delete_appointment로 별도 권한 검사를 거친다.

**함께 볼 파일**

- [application/controllers/Calendar.php](https://github.com/alextselegidis/easyappointments/blob/f6c8a4c2f364bf8c64b1f913a531a7134dcfd3c6/application/controllers/Calendar.php) — 관리자 예약 변경·삭제 및 권한 검사
- [application/libraries/Availability.php](https://github.com/alextselegidis/easyappointments/blob/f6c8a4c2f364bf8c64b1f913a531a7134dcfd3c6/application/libraries/Availability.php) — 등록·변경 시 후보 시간 계산
- [config-sample.php](https://github.com/alextselegidis/easyappointments/blob/f6c8a4c2f364bf8c64b1f913a531a7134dcfd3c6/config-sample.php) — DB 연결·URL 환경 설정 위치

**환경:** Easy!Appointments composer.json 표기 1.6.1. PHP >=8.2·MySQL·CodeIgniter 방식 서버, 화면은 jQuery·FullCalendar ^6.1.19·Moment. composer.json/package.json/config-sample.php를 함께 확인.

**한계·별도로 정할 것:** 취소 구현은 상태를 Cancelled로 보존하는 대신 실제 삭제한다. 취소 이력 보존이 요구되면 그대로 복사하면 안 된다. 예약 hash는 식별만 하는 공개 ID가 아니라 변경 권한에 관여하므로 노출을 제한해야 한다. 알림·외부 캘린더 연동 실패 복구도 별도 확인 대상이다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: GPL-3.0](https://github.com/alextselegidis/easyappointments/blob/f6c8a4c2f364bf8c64b1f913a531a7134dcfd3c6/LICENSE)

</details>

<a id="f-9-4"></a>

### 9-4. 겹치는 점검 시간을 저장하려 하면 경고하기

**예시 상황**

A-12에 오전 10~11시 예약이 있는데 담당자가 오전 10시 30분~11시 30분 예약을 추가하려는 상황이다.

**동작 예시**

1. 사용자가 새 점검의 시작·종료 시간을 입력하고 저장을 누른다.
2. 프로그램이 같은 설비의 기존 예약을 찾아 두 시간 구간이 겹치는지 비교한다.
3. 겹치는 예약이 있으면 사용자에게 충돌을 알리고 다른 시간을 고르게 하는 흐름을 만들 수 있다.

**참고 코드가 제공하는 부분**

원본에는 시간 구간의 겹침을 찾고 저장 전에 충돌을 알리는 처리가 있다. 다만 관리자 화면은 경고를 본 뒤에도 강제 저장할 수 있으므로, 원본 자체를 중복 예약 절대 금지 기능이라고 소개하면 안 된다.

**따로 만들거나 정할 부분**

설비별 예약에서 시작·종료 시간을 읽어 겹침을 비교하고, 수정 중인 예약 자신의 기록은 제외해야 한다. 강제 저장을 허용할지 과제 규칙으로 정한다. 두 사람이 동시에 저장하는 경우에도 중복을 막는 처리는 확인되지 않았으므로 필요하면 별도 구현·시험해야 한다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 시간 겹침 검사와 저장 전 충돌 안내

- **찾는 말:** 중복 예약 · 시간 겹침 · 충돌 · 예약 중복 · 동시 예약
- **언제 볼까:** 같은 담당자·자원에 겹치는 예약이 있는지 찾아 저장을 막거나 경고할 때.
- **자료 형태:** 예약 애플리케이션 구현 — 화면·서버·DB가 연결된 예제
- **저장소·확인 버전:** [alextselegidis/easyappointments](https://github.com/alextselegidis/easyappointments) · [`f6c8a4c2f364`](https://github.com/alextselegidis/easyappointments/commit/f6c8a4c2f364bf8c64b1f913a531a7134dcfd3c6)

**먼저 볼 코드**

- [application/models/Appointments_model.php](https://github.com/alextselegidis/easyappointments/blob/f6c8a4c2f364bf8c64b1f913a531a7134dcfd3c6/application/models/Appointments_model.php#L734-L766) — `has_provider_conflict`: 같은 제공자의 기존 시작<새 종료 AND 기존 종료>새 시작 조건으로 겹침을 조회한다.
- [application/controllers/Calendar.php](https://github.com/alextselegidis/easyappointments/blob/f6c8a4c2f364bf8c64b1f913a531a7134dcfd3c6/application/controllers/Calendar.php#L407-L452) — `save_appointment`: 충돌이면 conflict 응답을 반환하지만 force_save일 때 저장을 허용한다.
- [assets/js/http/calendar_http_client.js](https://github.com/alextselegidis/easyappointments/blob/f6c8a4c2f364bf8c64b1f913a531a7134dcfd3c6/assets/js/http/calendar_http_client.js) — `saveAppointmentWithConflictHandling`: 서버 충돌 응답 후 취소 또는 강제 저장을 선택하는 화면 흐름.

**참고할 부분과 선정 이유:** 참고할 핵심은 반열린 시간 구간의 겹침 조건과 수정 중인 예약 ID를 제외하는 방식이다. 예약 확정 직전에 검사하고 충돌 시 사용자에게 다시 선택하도록 안내한다. 단, 이 예제의 관리자 경로는 사용자가 강제 저장을 선택할 수 있으므로 ‘중복을 절대 허용하지 않는 규칙’과 구분한다.

**함께 볼 파일**

- [application/controllers/Booking.php](https://github.com/alextselegidis/easyappointments/blob/f6c8a4c2f364bf8c64b1f913a531a7134dcfd3c6/application/controllers/Booking.php) — 공개 예약 경로의 check_datetime_availability 재확인
- [application/libraries/Availability.php](https://github.com/alextselegidis/easyappointments/blob/f6c8a4c2f364bf8c64b1f913a531a7134dcfd3c6/application/libraries/Availability.php) — 예약 가능 시간 후보 생성

**환경:** Easy!Appointments composer.json 표기 1.6.1. PHP >=8.2·MySQL·CodeIgniter 방식 서버, 화면은 jQuery·FullCalendar ^6.1.19·Moment. composer.json/package.json/config-sample.php를 함께 확인.

**한계·별도로 정할 것:** 실제로 확인한 코드는 조회 후 저장 방식이며 여기서 트랜잭션 잠금/DB 제약으로 동시 요청의 중복을 원자적으로 차단한다는 증거는 확인하지 못했다. 이 항목은 겹침 검사·경고의 참조이며 동시 중복 예약 완전 방지의 완성 예제가 아니다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: GPL-3.0](https://github.com/alextselegidis/easyappointments/blob/f6c8a4c2f364bf8c64b1f913a531a7134dcfd3c6/LICENSE)

</details>

**아직 준비되지 않은 부분**

- 동시에 두 사람이 A-12의 같은 시간을 예약했을 때 반드시 한 사람만 성공하게 하는 처리는 확인하지 못했다. 중복을 절대 허용하지 않는 과제라면 저장 직전까지 충돌을 막는 처리와 동시 요청 시험이 추가로 필요하다.

<a id="category-10"></a>

## 10. 설비 수치의 이상을 판단할 재료와 알림 처리

A-12의 온도가 시간별로 들어오는 상황을 가정한다. 최근 수치로 평소 수준을 계산하는 일, 기준 초과를 이상으로 확정하는 일, 같은 알림을 반복해서 보내지 않는 일은 서로 다르다. 이 분류는 각 처리의 참고 자료이며 완성된 설비 감시 화면은 아니다.

<a id="f-anomaly-baseline"></a>

### 10-1. 최근 온도를 계산해 평소 수준과 비교하기

**예시 상황**

A-12의 최근 온도가 50도, 51도, 49도였고 새 값이 60도로 들어왔다. 담당자가 평소 수준에서 얼마나 달라졌는지 보고 싶은 상황이다.

**동작 예시**

1. 최근 세 값 50·51·49도의 평균을 계산하면 50도가 된다.
2. 세 값이 평균 주변에서 얼마나 흔들렸는지도 계산한다.
3. 새 값 60도를 이 계산 결과와 비교해 판단할 수 있다. 단, 이 예시만으로 60도가 반드시 이상이라고 확정하지 않는다.

**참고 코드가 제공하는 부분**

원본에는 최근 몇 개 값을 묶어 평균과 흔들림 정도를 계산하는 도구와 예제가 있다. 이상을 판정하기 위한 기준 수치를 만드는 데 쓰는 재료이며, 설비의 정상·이상을 최종 결정하는 완성 기능은 아니다.

**따로 만들거나 정할 부분**

측정 기록에서 설비 번호·측정 시각·온도를 읽어 시간 순서대로 계산에 넣어야 한다. 몇 개 값을 비교 기준으로 삼을지, 새 값을 기준 계산에 포함할지, 얼마나 벗어나면 이상인지 정한다. 값이 부족하거나 하나도 변하지 않는 경우의 처리도 필요하다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 평소 수준 비교를 위한 이동 통계

- **찾는 말:** 이상치 · 이동 평균 · 표준편차 · 평소 대비 · 센서
- **언제 볼까:** 최근 평균과 흔들림을 계산해 새 관측값과 비교할 때
- **자료 형태:** 라이브러리 함수·사용 예제 — 업무용 검사표·판정 화면은 조합해서 구현
- **저장소·확인 버전:** [pandas-dev/pandas](https://github.com/pandas-dev/pandas) · [`c32acd3c8371`](https://github.com/pandas-dev/pandas/commit/c32acd3c8371a1e33936dea9009d8eef6822ee81)

**먼저 볼 코드**

- [pandas/core/window/rolling.py](https://github.com/pandas-dev/pandas/blob/c32acd3c8371a1e33936dea9009d8eef6822ee81/pandas/core/window/rolling.py#L2664-L2740) — `Rolling.mean`: 창 크기별 이동 평균 예제
- [pandas/core/window/rolling.py](https://github.com/pandas-dev/pandas/blob/c32acd3c8371a1e33936dea9009d8eef6822ee81/pandas/core/window/rolling.py#L2808-L2880) — `Rolling.std`: 이동 표준편차 옵션과 설명
- [pandas/core/window/rolling.py](https://github.com/pandas-dev/pandas/blob/c32acd3c8371a1e33936dea9009d8eef6822ee81/pandas/core/window/rolling.py#L1757-L1779) — `RollingAndExpandingMixin.std`: 분산 후 제곱근 계산 구현

**참고할 부분과 선정 이유:** mean/std의 창 크기와 초기 결측값을 확인한다. 기준선을 구한 후 새 값과 비교하는 것은 이 API를 활용할 응용이다. 원본에 완성된 이상 탐지기가 있는 것은 아니다.

**함께 볼 파일**

- [pyproject.toml](https://github.com/pandas-dev/pandas/blob/c32acd3c8371a1e33936dea9009d8eef6822ee81/pyproject.toml) — Python·패키지 요구사항
- [pandas/core/tools/datetimes.py](https://github.com/pandas-dev/pandas/blob/c32acd3c8371a1e33936dea9009d8eef6822ee81/pandas/core/tools/datetimes.py#L847-L975) — 시간 순서·시간대 정리

**환경:** Python + pandas. 확인한 개발 커밋의 pyproject.toml은 Python >=3.11. 개발 브랜치 설치를 권하는 자료가 아니며 실전 설치 버전에서 사용할 API를 다시 확인한다.

**한계·별도로 정할 것:** 표준편차 0·초기 표본 부족·결측·추세/계절성·미래 데이터 섞임 정책이 필요하다. 현재 값을 기준선 계산에 포함할지도 정해야 한다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: BSD-3-Clause](https://github.com/pandas-dev/pandas/blob/c32acd3c8371a1e33936dea9009d8eef6822ee81/LICENSE)

</details>

<a id="f-alerts-threshold-state"></a>

### 10-2. 온도 초과가 계속될 때 이상으로 표시하고 복귀 기록하기

**예시 상황**

설명용으로 A-12가 80도를 넘는 상태가 3분간 계속될 때 알리기로 했다고 가정한다. 잠깐 81도가 됐다가 바로 내려온 경우와 지속되는 경우를 구분하려는 상황이다.

**동작 예시**

1. 80도 초과를 처음 확인하면 즉시 이상 확정하지 않고 지속 여부를 지켜보는 상태로 둔다.
2. 조건이 3분간 유지되면 이상 발생 상태로 바꾸고 관련 시각을 기록한다.
3. 이후 정상 범위로 돌아오면 해결된 상태와 복귀 시각을 기록한다.

**참고 코드가 제공하는 부분**

원본에는 조건 충족 후 일정 시간 기다리기, 이상 발생으로 바꾸기, 정상 복귀 처리라는 상태 전환이 있다. 위 80도·3분은 설명용 가정이며 원본 설비 기준이 아니다. 현재 해결되지 않은 이상을 추리는 방법도 참고한다.

**따로 만들거나 정할 부분**

온도 자료를 가져오는 주기와 이상 기준을 정하고, 설비별 이상 상태와 시작·복귀 시각을 보관해야 한다. 이 정보를 목록으로 보여 줄 화면과 문자·이메일로 보내는 연결은 이 항목에서 확인한 범위가 아니다. 필요하면 수신자를 정하고 실제 발송 결과까지 따로 확인해야 한다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 기준 초과 지속·알림 상태·정상 복귀

- **찾는 말:** 기준 초과 · 알림 상태 · 대기 · 발생 · 정상 복귀 · flapping
- **언제 볼까:** 일시적인 튐을 제외하고 일정 시간 지속된 이상과 복귀를 기록할 때
- **자료 형태:** 큰 서비스의 내부 처리 코드 — 알림 상태와 중복 처리 원리 참고
- **저장소·확인 버전:** [prometheus/prometheus](https://github.com/prometheus/prometheus) · [`3751fccd16d9`](https://github.com/prometheus/prometheus/commit/3751fccd16d96f5a584e9516d4b04eeaf4759a83)

**먼저 볼 코드**

- [docs/configuration/alerting_rules.md](https://github.com/prometheus/prometheus/blob/3751fccd16d96f5a584e9516d4b04eeaf4759a83/docs/configuration/alerting_rules.md#L17-L98) — `HighRequestLatency / InstanceDown`: 기준값·for·keep_firing_for·설명문 YAML
- [rules/alerting.go](https://github.com/prometheus/prometheus/blob/3751fccd16d96f5a584e9516d4b04eeaf4759a83/rules/alerting.go#L387-L549) — `AlertingRule.Eval`: pending/firing/inactive 전환과 ResolvedAt 기록
- [rules/alerting.go](https://github.com/prometheus/prometheus/blob/3751fccd16d96f5a584e9516d4b04eeaf4759a83/rules/alerting.go#L573-L582) — `AlertingRule.ActiveAlerts`: 현재 미해결 알림 목록

**참고할 부분과 선정 이유:** YAML의 조건→지속시간→설명을 먼저 읽고 Eval 상태 전환을 본다. ActiveAlerts는 미해결 알림 목록의 기초다. 간단한 앱에서는 상태 관리 원리를 참고하며 Prometheus 전체 설치나 Go 내부 파일 복사를 기본으로 삼지 않는다.

**함께 볼 파일**

- [go.mod](https://github.com/prometheus/prometheus/blob/3751fccd16d96f5a584e9516d4b04eeaf4759a83/go.mod) — 원본 Go 버전 및 의존성
- [rules/alerting.go](https://github.com/prometheus/prometheus/blob/3751fccd16d96f5a584e9516d4b04eeaf4759a83/rules/alerting.go#L80-L100) — Alert 구조의 상태와 시간 필드

**환경:** Go/Prometheus/PromQL 기반. 확인한 go.mod는 Go 1.26.10. YAML을 실제 사용하려면 Prometheus와 해당 시계열 수집 설정 필요.

**한계·별도로 정할 것:** 측정값 이름은 샘플이다. 외부 발송은 Alertmanager 등 별도 경로. 알림 목록 화면 구현은 이 항목에서 검증하지 않았다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: Apache-2.0](https://github.com/prometheus/prometheus/blob/3751fccd16d96f5a584e9516d4b04eeaf4759a83/LICENSE)

</details>

<a id="f-alerts-dedup-recovery"></a>

### 10-3. 같은 이상 알림은 줄이고 오래 지속되거나 해결되면 다시 알리기

**예시 상황**

A-12의 같은 온도 이상이 매분 확인되더라도 매분 같은 알림을 받고 싶지는 않은 상황이다. 설명용으로 최초 발생, 30분 뒤에도 지속, 해결 시점에만 알려 주고 싶다고 가정한다.

**동작 예시**

1. 처음 발생한 A-12 이상을 알리고, 누구에게 언제 어떤 이상을 보냈는지 남긴다.
2. 1분 뒤 상태가 같으면 이전 발송 기록과 비교해 반복 발송을 건너뛴다.
3. 정한 재알림 시간이 지났거나 이상이 해결되면 다시 보낼 대상으로 판단한다.

**참고 코드가 제공하는 부분**

원본에는 이전에 보낸 알림과 현재 발생·해결 목록, 마지막 발송 시간을 비교해 다시 보낼지 판단하는 처리가 있다. 발송이 끝난 뒤 기록을 남기는 처리까지 함께 참고한다. 30분이라는 값은 설명용 선택이며 원본의 보장값이 아니다.

**따로 만들거나 정할 부분**

어떤 설비의 어떤 이상을 같은 알림으로 볼지 정하고, 수신자·마지막 발송 시각·발생 또는 해결 상태를 저장해야 한다. 실제 발송과 저장이 실패했을 때 어떻게 다시 처리할지, 프로그램을 재시작해도 이 기록을 유지할지 따로 구현·시험한다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 중복 억제·재알림·해결 알림

- **찾는 말:** 중복 알림 · 재알림 · 해결 · 알림 이력 · dedup
- **언제 볼까:** 같은 이상은 반복 발송하지 않고 변경·해결·재알림 시점에만 처리할 때
- **자료 형태:** 큰 서비스의 내부 처리 코드 — 알림 상태와 중복 처리 원리 참고
- **저장소·확인 버전:** [prometheus/alertmanager](https://github.com/prometheus/alertmanager) · [`b13545770266`](https://github.com/prometheus/alertmanager/commit/b13545770266ae675aac61c9d7612a2778dcf24d)

**먼저 볼 코드**

- [notify/dedup_stage.go](https://github.com/prometheus/alertmanager/blob/b13545770266ae675aac61c9d7612a2778dcf24d/notify/dedup_stage.go#L31-L175) — `DedupStage.needsUpdate / partitionAlertsByState / Exec`: 이전 기록과 발생/해결 집합·재알림 시간 비교
- [notify/set_notifies_stage.go](https://github.com/prometheus/alertmanager/blob/b13545770266ae675aac61c9d7612a2778dcf24d/notify/set_notifies_stage.go#L64-L105) — `SetNotifiesStage.Exec`: 발송 이후 알림 이력 저장
- [notify/notify_test.go](https://github.com/prometheus/alertmanager/blob/b13545770266ae675aac61c9d7612a2778dcf24d/notify/notify_test.go#L103-L226) — `TestDedupStageNeedsUpdate`: 동일 알림의 시간 전후·신규·해결별 기대값

**참고할 부분과 선정 이유:** needsUpdate 분기를 테스트의 기대값과 대조한다. 그룹 ID·수신 대상·발생/해결 목록·마지막 발송 시각이 필요하다. 발송 성공 후 저장하는 SetNotifiesStage까지 함께 봐야 중복 억제가 유지되는 이유를 이해할 수 있다.

**함께 볼 파일**

- [notify/notify.go](https://github.com/prometheus/alertmanager/blob/b13545770266ae675aac61c9d7612a2778dcf24d/notify/notify.go) — Dedup→Retry→SetNotifies 단계 조립
- [go.mod](https://github.com/prometheus/alertmanager/blob/b13545770266ae675aac61c9d7612a2778dcf24d/go.mod) — Go 버전 및 의존성

**환경:** Go Alertmanager. 확인한 go.mod는 Go 1.26.0. NotificationLog, alert 구조, 수신자·컨텍스트·재시도 단계에 의존.

**한계·별도로 정할 것:** 큰 시스템의 원리 참고용이며 독립 함수로 바로 붙일 수 없다. DB로 단순화한다면 저장·실패·재시작 정책을 다시 설계한다. 실제 발송·동시성·복구 실행은 미검증.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: Apache-2.0](https://github.com/prometheus/alertmanager/blob/b13545770266ae675aac61c9d7612a2778dcf24d/LICENSE)

</details>

**아직 준비되지 않은 부분**

- 측정값 수집부터 이상 판정, 알림 목록 화면, 실제 메시지 발송까지 이어지는 완성 프로그램은 없다. 최근 수치를 계산하는 방법과 알림 상태·반복 발송을 관리하는 부분을 각각 참고한다.

<a id="category-11"></a>

## 11. 다른 시스템의 점검 요청을 가져오고 반복 처리하기

우리 프로그램 밖의 업무 시스템에 점검 요청 자료가 있다고 가정한다. 자료를 한 번 가져오는 처리와, 5분마다 반복하는 처리, 실패했을 때 다시 시도하는 처리는 별개다. 이 분류는 연결과 작업 실행 방법을 제공하며 특정 사내 시스템에 이미 연결된 완성 프로그램은 아니다.

<a id="f-integration-http"></a>

### 11-1. 다른 시스템에서 점검 요청을 가져오거나 처리 결과 보내기

**예시 상황**

담당자가 외부 요청 가져오기를 누르면 다른 시스템에 있는 요청 R-001의 설비·요청 내용·접수일을 받아 우리 목록에 반영하고 싶은 상황이다.

**동작 예시**

1. 다른 시스템에 가져올 기간이나 요청 번호 조건을 보낸다.
2. 받은 응답이 성공인지 확인하고 그 안의 요청 자료를 읽는다.
3. 필요하면 우리 프로그램에서 처리한 결과도 다른 시스템에 보내는 흐름을 만들 수 있다.

**참고 코드가 제공하는 부분**

원본에는 조회 조건을 보내 자료를 받거나 자료를 전송하고, 연결 실패와 상대 시스템의 오류 응답을 구분하는 방법이 있다. 실제 점검 요청을 읽고 우리 요청 목록에 저장하는 코드는 아니다.

**따로 만들거나 정할 부분**

연결할 시스템의 주소와 접속 권한, 설비·접수일·상태가 어떤 이름으로 전달되는지 알아야 한다. 받은 항목을 우리 요청 저장소의 항목에 맞추고 R-001이 이미 있으면 새로 만들지 수정할지 정한다. 응답을 읽었다고 저장까지 성공한 것은 아니며 전송을 반복할 때의 중복 처리도 별도로 막아야 한다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 외부 API 읽기·JSON 전송·응답 오류 구분

- **찾는 말:** API · 외부 연결 · GET · POST · JSON · timeout · 데이터 가져오기
- **언제 볼까:** 다른 시스템에 조건을 보내 데이터를 받거나, 처리 결과를 JSON으로 보낼 때
- **자료 형태:** 라이브러리 함수·공식 호출 예제 — 실제 연동 대상은 별도
- **저장소·확인 버전:** [encode/httpx](https://github.com/encode/httpx) · [`b5addb64f016`](https://github.com/encode/httpx/commit/b5addb64f0161ff6bfe94c124ef76f6a1fba5254)

**먼저 볼 코드**

- [httpx/_api.py](https://github.com/encode/httpx/blob/b5addb64f0161ff6bfe94c124ef76f6a1fba5254/httpx/_api.py) — `request / get / post`: 주소·쿼리 조건·JSON 본문·timeout 등을 HTTP 요청으로 전달한다.
- [httpx/_models.py](https://github.com/encode/httpx/blob/b5addb64f0161ff6bfe94c124ef76f6a1fba5254/httpx/_models.py) — `Response.raise_for_status / Response.json`: 성공하지 않은 응답을 오류로 구분하고 JSON 본문을 읽는다.
- [docs/quickstart.md](https://github.com/encode/httpx/blob/b5addb64f0161ff6bfe94c124ef76f6a1fba5254/docs/quickstart.md) — `Passing Parameters In URLs / JSON Response Content / Sending JSON Encoded Data / Exceptions`: 위 API를 실제 호출 형태로 쓰는 공식 코드 예제

**참고할 부분과 선정 이유:** GET의 params로 조회 조건을 보내고 응답 상태를 확인한 뒤 json()으로 데이터를 읽는 흐름, POST의 json으로 자료를 전송하는 흐름을 참고한다. 연결 실패와 서버의 오류 응답, 응답 데이터의 형식 오류는 서로 다른 실패로 처리한다.

**함께 볼 파일**

- [pyproject.toml](https://github.com/encode/httpx/blob/b5addb64f0161ff6bfe94c124ef76f6a1fba5254/pyproject.toml) — Python·라이브러리 요구사항

**환경:** Python + HTTPX. 확인한 pyproject.toml은 Python >=3.9와 httpcore·anyio·certifi·idna 등을 선언한다. 연결할 외부 서비스의 주소·인증·데이터 형식은 별도 필요하다.

**한계·별도로 정할 것:** 외부 서비스의 필드·인증·페이지 이동·요청 제한은 이 라이브러리가 대신 정해주지 않는다. JSON 파싱 성공과 원하는 데이터 구조의 일치는 다르다. 자동 재시도나 중복 전송 방지가 있다는 뜻이 아니며, POST 재시도는 중복 처리 위험을 따로 검토한다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: BSD-3-Clause](https://github.com/encode/httpx/blob/b5addb64f0161ff6bfe94c124ef76f6a1fba5254/LICENSE.md)

</details>

<a id="f-integration-periodic"></a>

### 11-2. 정해진 시간 간격으로 새 점검 요청 확인하기

**예시 상황**

담당자가 버튼을 매번 누르지 않아도 외부 시스템의 새 점검 요청이 우리 목록에 나타나게 하고 싶은 상황이다.

**동작 예시**

1. 새 요청을 확인하는 작업과 5분이라는 실행 간격을 등록한다.
2. 시간을 관리하는 부분이 5분마다 작업을 실행하도록 전달하고, 작업을 맡는 부분이 실제 확인을 수행한다.
3. 실제 가져오기와 저장 처리를 연결하면 새 요청이 우리 목록에 반영되는 흐름을 만들 수 있다.

**참고 코드가 제공하는 부분**

원본은 정해진 간격으로 문장을 출력하는 단순 작업 예제다. 어떤 작업을 언제 반복할지 등록하고 작업 실행을 나누는 방법을 참고한다. 외부 점검 요청을 가져와 저장하는 기능은 원본에 완성되어 있지 않다.

**따로 만들거나 정할 부분**

외부 시스템에서 지난 확인 이후의 요청을 읽고 우리 요청 저장소에 추가·수정하는 작업을 먼저 만들어 연결해야 한다. 반복 실행을 맡는 별도 환경도 필요하다. 이전 확인 작업이 아직 끝나지 않았는데 다음 실행 시각이 된 경우와 중단 후 빠진 기간을 어떻게 처리할지 정한다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 정해진 주기로 작업 실행하기

- **찾는 말:** 주기 실행 · 일정 실행 · 자동 갱신 · 동기화 · 배치 · 스케줄
- **언제 볼까:** 몇 분마다 데이터를 확인하거나 정해진 주기로 처리 함수를 실행할 때
- **자료 형태:** 공식 작업 실행 예제 — 메시지 서버·worker가 필요
- **저장소·확인 버전:** [celery/celery](https://github.com/celery/celery) · [`2ef8265b0a1d`](https://github.com/celery/celery/commit/2ef8265b0a1dd977abdbcb087d3208b6575842c1)

**먼저 볼 코드**

- [examples/periodic-tasks/myapp.py](https://github.com/celery/celery/blob/2ef8265b0a1dd977abdbcb087d3208b6575842c1/examples/periodic-tasks/myapp.py) — `setup_periodic_tasks / say`: 10초 간격 작업을 등록하고 스케줄러와 worker를 나눠 실행하는 예제

**참고할 부분과 선정 이유:** setup_periodic_tasks에서 함수와 실행 간격을 연결하는 방식을 참고한다. 스케줄을 보내는 beat와 작업을 처리하는 worker가 나뉜다. say는 문장을 출력하는 예제이므로, 실제 데이터 수집·갱신 함수는 과제에 맞춰 구현한다.

**함께 볼 파일**

- [examples/next-steps/proj/celery.py](https://github.com/celery/celery/blob/2ef8265b0a1dd977abdbcb087d3208b6575842c1/examples/next-steps/proj/celery.py) — 메시지 서버·결과 저장소·작업 모듈을 지정하는 별도 앱 설정 예시

**환경:** Python·Celery. 메시지를 전달하는 별도 서버(broker)와 작업을 실행하는 worker가 필요하고, 결과를 조회하려면 결과 저장소 설정도 필요하다. 작은 과제의 단순 반복 작업에 전체 Celery 도입이 필요한지는 별도 판단한다.

**한계·별도로 정할 것:** 데이터 동기화 기능 자체가 완성된 예제는 아니다. 이전 작업이 끝나기 전에 다음 작업이 시작되는 경우, 중복 실행, 중단 후 재개 정책은 별도 설계한다. 시간대는 예제의 UTC를 그대로 쓰지 말고 과제 조건과 맞춘다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: 코드 BSD-3-Clause / 렌더링된 문서 CC BY-SA-4.0](https://github.com/celery/celery/blob/2ef8265b0a1dd977abdbcb087d3208b6575842c1/LICENSE)

</details>

<a id="f-integration-batch"></a>

### 11-3. 여러 요청 파일을 나누어 처리하고 결과 모으기

**예시 상황**

담당자가 점검 요청 파일 여러 개를 올렸을 때 파일마다 검사하고, 끝난 결과를 한곳에서 모아 보고 싶은 상황이다.

**동작 예시**

1. 설명용으로 요청 파일 3개를 각각 하나의 처리 작업으로 나눈다.
2. 여러 작업을 묶어 실행하고 결과를 모으거나, 첫 작업의 결과를 다음 작업에 넘겨 순서대로 처리한다.
3. 파일 검사 결과를 화면에 모으는 부분까지 연결하면 담당자가 처리 결과를 확인할 수 있다.

**참고 코드가 제공하는 부분**

원본은 덧셈·곱셈 같은 계산을 여러 개 묶어 실행하거나 앞 계산 결과를 다음 계산에 넘기는 예제다. 여러 파일을 읽고 검사하는 완성 프로그램은 아니며 작업을 묶고 이어 주는 방식을 참고한다.

**따로 만들거나 정할 부분**

업로드된 각 파일을 어디에 저장할지 정하고, 파일을 읽어 검사 결과를 만드는 작업을 구현해야 한다. 파일별 결과를 저장한 뒤 화면에서 모아 보여 주는 부분도 만든다. 한 파일만 실패했을 때 재처리할 범위, 진행률 표시, 같은 파일의 중복 처리는 별도로 정한다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 여러 작업 일괄 실행·결과 모으기·순서 연결

- **찾는 말:** 일괄 처리 · 병렬 작업 · 작업 큐 · group · chain · 대량 처리
- **언제 볼까:** 여러 파일을 각각 처리한 결과를 모으거나 앞 작업의 결과를 다음 작업에 넘길 때
- **자료 형태:** 공식 작업 실행 예제 — 메시지 서버·worker가 필요
- **저장소·확인 버전:** [celery/celery](https://github.com/celery/celery) · [`2ef8265b0a1d`](https://github.com/celery/celery/commit/2ef8265b0a1dd977abdbcb087d3208b6575842c1)

**먼저 볼 코드**

- [examples/next-steps/proj/tasks.py](https://github.com/celery/celery/blob/2ef8265b0a1dd977abdbcb087d3208b6575842c1/examples/next-steps/proj/tasks.py) — `add / mul / xsum`: 작업으로 등록한 계산 함수 예제
- [docs/getting-started/next-steps.rst](https://github.com/celery/celery/blob/2ef8265b0a1dd977abdbcb087d3208b6575842c1/docs/getting-started/next-steps.rst) — `Groups / Chains 코드 블록`: group으로 작업들을 묶어 결과를 모으고 chain으로 앞 결과를 다음 작업에 전달하는 호출 예제

**참고할 부분과 선정 이유:** group(add.s(i, i) ...) 형태는 입력마다 작업을 만들어 한 번에 제출하는 방식이다. chain의 add → mul 연결은 앞 결과를 뒤 작업으로 넘기는 방식이다. 계산 함수를 실제 파일 처리 함수로 바꾸는 것은 과제의 응용이며, 원본에 완성된 파일 일괄 처리 앱이 있는 것은 아니다.

**함께 볼 파일**

- [examples/next-steps/proj/celery.py](https://github.com/celery/celery/blob/2ef8265b0a1dd977abdbcb087d3208b6575842c1/examples/next-steps/proj/celery.py) — proj.tasks 등록과 broker·결과 저장소 설정

**환경:** Python·Celery. 메시지를 전달하는 별도 서버(broker)와 작업을 실행하는 worker가 필요하고, 결과를 조회하려면 결과 저장소 설정도 필요하다. 작은 과제의 단순 반복 작업에 전체 Celery 도입이 필요한지는 별도 판단한다.

**한계·별도로 정할 것:** 일부 실패 후 전체 취소·재처리, 처리 중 진행률 화면, 같은 입력의 중복 처리 방지는 별도다. 문서의 chord까지 포함한 모든 조합이 예제의 rpc 결과 저장소에서 작동한다는 뜻은 아니다. 여기서는 group·chain 호출 예제만 안내한다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: 코드 BSD-3-Clause / 렌더링된 문서 CC BY-SA-4.0](https://github.com/celery/celery/blob/2ef8265b0a1dd977abdbcb087d3208b6575842c1/LICENSE)

</details>

<a id="f-integration-retry"></a>

### 11-4. 외부 시스템이 잠깐 멈추면 기다렸다 다시 요청하기

**예시 상황**

외부 시스템에서 R-001을 가져오려는데 일시적으로 연결이 끊겼다. 바로 실패로 끝내지 않고 정해진 횟수만 다시 시도하려는 상황이다.

**동작 예시**

1. 실패 이유를 확인해 잠시 후 다시 해 볼 오류인지, 권한 부족처럼 다시 해도 해결되지 않을 오류인지 나눈다.
2. 다시 시도할 오류이면 기다렸다 요청하고, 반복 실패할수록 대기 시간을 늘린다.
3. 정해진 최대 재시도 횟수에 도달하면 중단하고 실패 결과를 남기는 흐름을 구성한다.

**참고 코드가 제공하는 부분**

원본에는 다시 시도할 오류와 제외할 오류를 구분하고, 시도 횟수에 따라 기다리는 시간을 늘리는 처리가 있다. 큰 작업 실행 도구 안에 들어 있는 부분이므로 해당 파일만 복사하면 독립적으로 작동하는 예제는 아니다.

**따로 만들거나 정할 부분**

외부 요청 실패를 이 처리에 전달하고, 최대 횟수와 최종 실패를 어디에 기록할지 정해야 한다. 조회 재시도와 등록 재시도를 구분한다. 예를 들어 R-001 전송은 성공했지만 응답만 못 받은 경우 다시 보내면 두 번 등록될 수 있으므로 같은 요청인지 확인하는 별도 규칙이 필요하다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 실패 종류별 재시도·대기시간 늘리기

- **찾는 말:** 재시도 · 외부 실패 · backoff · 일시 오류 · retry · 지수 대기
- **언제 볼까:** 일시적인 외부 오류만 정해진 횟수 안에서 다시 시도하려 할 때
- **자료 형태:** 작업 처리 라이브러리 내부 구현 — 재시도 원리 참고
- **저장소·확인 버전:** [celery/celery](https://github.com/celery/celery) · [`2ef8265b0a1d`](https://github.com/celery/celery/commit/2ef8265b0a1dd977abdbcb087d3208b6575842c1)

**먼저 볼 코드**

- [celery/app/autoretry.py](https://github.com/celery/celery/blob/2ef8265b0a1dd977abdbcb087d3208b6575842c1/celery/app/autoretry.py) — `add_autoretry_behaviour`: 다시 시도할 예외와 제외할 예외를 나누고 대기시간을 계산해 task.retry를 호출한다.
- [celery/utils/time.py](https://github.com/celery/celery/blob/2ef8265b0a1dd977abdbcb087d3208b6575842c1/celery/utils/time.py) — `get_exponential_backoff_interval`: 시도 횟수에 따라 대기시간을 늘리고 상한·무작위 분산을 적용한다.

**참고할 부분과 선정 이유:** autoretry_for와 dont_autoretry_for로 일시 장애와 재시도해도 해결되지 않는 실패를 구분하는 구조를 참고한다. backoff는 재시도가 몰리지 않도록 기다리는 시간을 점차 늘리는 방식이다. 이 파일은 Celery 내부 구현이므로 함수 전체를 독립 코드처럼 복사하지 않는다.

**함께 볼 파일**

- [examples/next-steps/proj/tasks.py](https://github.com/celery/celery/blob/2ef8265b0a1dd977abdbcb087d3208b6575842c1/examples/next-steps/proj/tasks.py) — 재시도 정책을 적용할 대상인 작업 함수의 등록 형태
- [examples/next-steps/proj/celery.py](https://github.com/celery/celery/blob/2ef8265b0a1dd977abdbcb087d3208b6575842c1/examples/next-steps/proj/celery.py) — 작업 실행 환경 설정

**환경:** Python·Celery. 메시지를 전달하는 별도 서버(broker)와 작업을 실행하는 worker가 필요하고, 결과를 조회하려면 결과 저장소 설정도 필요하다. 작은 과제의 단순 반복 작업에 전체 Celery 도입이 필요한지는 별도 판단한다.

**한계·별도로 정할 것:** 다시 보내도 중복 생성·중복 결제가 없다는 보장은 없다. 최대 재시도·시간 제한·재시도 허용 실패를 과제에서 정하고, 데이터 쓰기에는 중복 방지 규칙을 따로 둔다. 예제 계산 함수에 재시도가 이미 설정되어 있다는 뜻도 아니다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: 코드 BSD-3-Clause / 렌더링된 문서 CC BY-SA-4.0](https://github.com/celery/celery/blob/2ef8265b0a1dd977abdbcb087d3208b6575842c1/LICENSE)

</details>

**아직 준비되지 않은 부분**

- 어느 사내 시스템에 접속할 수 있는지와 실제 자료 형식은 확인하지 않았다. 외부 요청과 우리 요청 중 값이 다를 때 어느 쪽을 따를지, 같은 요청을 다시 받아도 중복 저장하지 않는 방법은 따로 만들어야 한다.

<a id="category-12"></a>

## 12. 누가 볼 수 있고 바꿀 수 있는지 정하고 변경 내용 남기기

요청자·점검 담당자·관리자가 같은 요청 관리 프로그램을 사용한다고 가정한다. 로그인으로 사용자를 확인하고, 그 사용자가 R-001을 볼 수 있는지 또는 수정할 수 있는지 검사한다. 수정 이력은 실제 요청 자료와 연결해서 언제 무엇이 바뀌었는지 확인하는 데 쓴다.

<a id="f-12-1"></a>

### 12-1. 로그인한 사용자를 확인하고 로그아웃하기

**예시 상황**

김민수가 로그인 화면에서 본인 계정으로 들어오고, 일을 마치면 로그아웃하려는 상황이다.

**동작 예시**

1. 입력한 로그인 정보가 맞는지 확인한다. 실패했거나 비활성 계정이면 로그인을 거절한다.
2. 성공하면 이후 목록 조회·수정 동작을 로그인한 김민수가 했음을 확인할 수 있게 연결한다.
3. 로그아웃하면 해당 로그인 연결을 끝낸다.

**참고 코드가 제공하는 부분**

원본에는 로그인 정보 검사, 실패 추적, 로그인한 사용자와 이후 요청의 연결, 로그아웃 처리가 있다. 큰 업무 프로그램의 로그인 흐름을 참고하는 자료이며 짧은 로그인 예제 하나를 바로 가져오는 방식은 아니다.

**따로 만들거나 정할 부분**

사용할 계정이 회사 계정인지 프로그램 안에서 관리하는 계정인지 정하고, 로그인 결과를 이후 요청 처리에서 확인하도록 연결해야 한다. 원본의 일부만 떼면 만료 시간이나 추가 인증 같은 보호가 빠질 수 있다. 로그인한 사람이 R-001을 수정해도 되는지는 다음 항목의 권한 검사로 별도 판단한다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 로그인·로그아웃·세션 연결

- **찾는 말:** 로그인 · 로그아웃 · 인증 · 세션 · 비밀번호
- **언제 볼까:** 로그인한 사용자와 요청을 연결하고 잘못된 인증 요청을 거절해야 할 때.
- **자료 형태:** 큰 업무 프레임워크의 구현 — 데이터·권한 구조와 함께 참고
- **저장소·확인 버전:** [frappe/frappe](https://github.com/frappe/frappe) · [`667fbb59e429`](https://github.com/frappe/frappe/commit/667fbb59e429e45592f02373729188d1c62d2a47)

**먼저 볼 코드**

- [frappe/auth.py](https://github.com/frappe/frappe/blob/667fbb59e429e45592f02373729188d1c62d2a47/frappe/auth.py) — `LoginManager.login / authenticate / post_login / logout`: 입력 인증, 비활성 사용자 거절, 실패 횟수 추적, 세션 발급과 종료.
- [frappe/sessions.py](https://github.com/frappe/frappe/blob/667fbb59e429e45592f02373729188d1c62d2a47/frappe/sessions.py#L294-L364) — `Session.start / insert_session_record`: 서버 세션을 사용자와 연결하고 만료 관련 데이터를 저장한다.

**참고할 부분과 선정 이유:** LoginManager.login→authenticate→post_login→make_session 순서로 읽는다. 인증 성공 전에는 사용자 정보나 권한을 믿지 않고, 성공한 사용자에 한해 세션을 만드는 경계를 참고한다. 비밀번호 자체를 비교/기록하는 예제로 쓰지 말고 utils/password.py의 검증 함수를 포함한 인증 라이브러리 호출 구조를 본다.

**함께 볼 파일**

- [frappe/utils/password.py](https://github.com/frappe/frappe/blob/667fbb59e429e45592f02373729188d1c62d2a47/frappe/utils/password.py) — 비밀번호 검증·해시 갱신
- [pyproject.toml](https://github.com/frappe/frappe/blob/667fbb59e429e45592f02373729188d1c62d2a47/pyproject.toml) — 인증·웹 서버·DB 관련 의존성

**환경:** Python·JavaScript 기반 Frappe 전체 프레임워크 코드. 이 커밋 pyproject.toml은 Python >=3.14,<3.15와 DB 드라이버·Redis·RQ 등을 요구한다. 개별 함수만 복사해 실행할 수 있는 독립 예제가 아니다.

**한계·별도로 정할 것:** Frappe 환경에 결합된 인증 전체 흐름의 참고 자료다. 일부 함수만 떼면 쿠키 설정·CSRF·2단계 인증·세션 만료 등의 보장이 사라질 수 있다. 이 코드를 읽었다고 보안 검증 완료로 표시하지 않는다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: MIT](https://github.com/frappe/frappe/blob/667fbb59e429e45592f02373729188d1c62d2a47/LICENSE)

</details>

<a id="f-12-2"></a>

### 12-2. 담당자에게는 자기 요청만, 관리자에게는 전체 요청 보이기

**예시 상황**

설명용으로 김민수는 자신이 담당한 R-001만 수정할 수 있고, 관리자는 모든 요청을 볼 수 있다고 정한 상황이다.

**동작 예시**

1. 김민수가 목록을 열면 자신에게 허용된 요청을 조건으로 걸러 보여 준다.
2. 다른 사람의 요청 주소를 직접 입력해도 그 요청을 볼 권한이 있는지 다시 확인한다.
3. R-001을 수정하려 할 때도 읽기 허용과 별도로 수정 권한을 검사한 뒤 저장한다.

**참고 코드가 제공하는 부분**

원본에는 사용자의 역할, 해당 자료의 소유자나 담당 관계, 공유 여부를 함께 보고 읽기·쓰기 가능 여부를 계산하는 처리가 있다. 목록에 조건을 거는 검사와 개별 자료를 직접 열었을 때의 검사를 함께 두는 방법을 참고한다.

**따로 만들거나 정할 부분**

우리 계정에 역할을 저장하고 요청마다 요청자·담당자를 기록해야 한다. 목록 조회·상세 열기·수정 저장 각각에서 이 정보로 권한을 확인하게 연결한다. 담당자는 자기 요청만 수정한다는 규칙은 설명용 가정이므로 실제 과제에서 합의해야 하며 버튼을 숨기는 것만으로 끝내면 안 된다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 역할별 동작 제한·개별 데이터 접근 제한

- **찾는 말:** 권한 · 역할 · 관리자 · 본인 데이터 · 접근 제한 · 읽기 권한 · 쓰기 권한
- **언제 볼까:** 관리자/담당자/조회자마다 가능한 동작이 다르거나 자기 담당 데이터만 보여야 할 때.
- **자료 형태:** 큰 업무 프레임워크의 구현 — 데이터·권한 구조와 함께 참고
- **저장소·확인 버전:** [frappe/frappe](https://github.com/frappe/frappe) · [`667fbb59e429`](https://github.com/frappe/frappe/commit/667fbb59e429e45592f02373729188d1c62d2a47)

**먼저 볼 코드**

- [frappe/permissions.py](https://github.com/frappe/frappe/blob/667fbb59e429e45592f02373729188d1c62d2a47/frappe/permissions.py#L82-L356) — `has_permission / get_doc_permissions / get_role_permissions / has_user_permission`: 역할 권한에 문서 소유자·사용자 제한·공유 권한 등을 결합해 동작별 허용 여부를 계산한다.
- [frappe/desk/doctype/todo/todo.py](https://github.com/frappe/frappe/blob/667fbb59e429e45592f02373729188d1c62d2a47/frappe/desk/doctype/todo/todo.py#L151-L176) — `get_permission_query_conditions / has_permission`: 목록 조회 조건과 단일 항목 접근 검사를 함께 두는 구체 예.

**참고할 부분과 선정 이유:** has_permission의 ptype(읽기/쓰기 등)과 doc(대상 데이터)을 별도 입력으로 두는 구조부터 본다. todo.py는 목록에서는 allocated_to/assigned_by/owner 조건을 걸고, 단건에서도 같은 관계를 검사한다. 화면에서 버튼을 숨기는 것만으로 끝내지 말고 목록 API와 ID로 직접 접근하는 상세·수정 API 모두에 같은 업무 권한을 적용하는 데 참고한다.

**함께 볼 파일**

- [frappe/desk/form/assign_to.py](https://github.com/frappe/frappe/blob/667fbb59e429e45592f02373729188d1c62d2a47/frappe/desk/form/assign_to.py) — 실제 변경 함수에서 문서 권한을 호출하는 위치
- [frappe/workflow/doctype/workflow_action/workflow_action.py](https://github.com/frappe/frappe/blob/667fbb59e429e45592f02373729188d1c62d2a47/frappe/workflow/doctype/workflow_action/workflow_action.py) — 승인 대기 항목의 역할 기반 목록·단건 검사

**환경:** Python·JavaScript 기반 Frappe 전체 프레임워크 코드. 이 커밋 pyproject.toml은 Python >=3.14,<3.15와 DB 드라이버·Redis·RQ 등을 요구한다. 개별 함수만 복사해 실행할 수 있는 독립 예제가 아니다.

**한계·별도로 정할 것:** Administrator·공유·소유자 등의 예외가 있으므로 함수 이름만 보고 ‘역할만 맞으면 된다’고 단순화하지 않는다. 실제 조직 역할과 승인 권한은 사용자 합의 내용으로 정해야 한다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: MIT](https://github.com/frappe/frappe/blob/667fbb59e429e45592f02373729188d1c62d2a47/LICENSE)

</details>

<a id="f-12-3"></a>

### 12-3. 요청의 수정 전후 내용을 기록하기

**예시 상황**

담당자가 R-001의 상태를 미처리에서 완료로 바꾸거나 점검 항목을 추가했을 때, 나중에 변경 내용을 확인하려는 상황이다.

**동작 예시**

1. 저장하기 전 R-001의 값과 저장할 새 값을 비교한다.
2. 상태는 미처리→완료처럼 값의 변경으로 남기고, 점검 항목을 추가하거나 지운 것은 별도 구분해 남긴다.
3. 변경 기록을 R-001과 연결해 해당 요청의 이전·이후 내용을 찾아볼 수 있게 한다.

**참고 코드가 제공하는 부분**

원본에는 이전 문서와 현재 문서를 비교해 바뀐 값, 추가된 행, 삭제된 행을 기록하는 부분이 있다. 기록을 남길지 설정을 확인한 뒤 대상 자료와 연결해 저장하는 방식을 참고한다.

**따로 만들거나 정할 부분**

우리 요청을 저장할 때 이전 값을 확보하고 비교 결과를 변경 기록 저장소에 남겨야 한다. 누가 변경했는지까지 보려면 로그인 사용자나 업무 처리자 정보도 함께 연결하고, 기록을 볼 화면을 만든다. 원본에도 기록하지 않는 조건이 있으므로 모든 변경의 영구 보존이나 기록 조작 방지가 보장되는 자료는 아니다.

<details>
<summary>AI가 참고할 기술 정보 — 코드 위치·관련 파일·사용 조건</summary>

**기술 항목명:** 값 변경 이력·추가/삭제된 행 기록

- **찾는 말:** 변경 기록 · 감사 이력 · 수정 이력 · 누가 변경 · 이전 값 · 변경 후 값
- **언제 볼까:** 중요 데이터가 바뀌었을 때 이전 값과 이후 값, 변경 항목을 확인해야 할 때.
- **자료 형태:** 큰 업무 프레임워크의 구현 — 데이터·권한 구조와 함께 참고
- **저장소·확인 버전:** [frappe/frappe](https://github.com/frappe/frappe) · [`667fbb59e429`](https://github.com/frappe/frappe/commit/667fbb59e429e45592f02373729188d1c62d2a47)

**먼저 볼 코드**

- [frappe/core/doctype/version/version.py](https://github.com/frappe/frappe/blob/667fbb59e429e45592f02373729188d1c62d2a47/frappe/core/doctype/version/version.py#L30-L219) — `Version.update_version_info / set_diff / get_diff`: 일반 필드 변경과 하위 표의 추가·삭제·변경을 비교해 구조화된 기록으로 만든다.
- [frappe/model/document.py](https://github.com/frappe/frappe/blob/667fbb59e429e45592f02373729188d1c62d2a47/frappe/model/document.py#L2337-L2361) — `Document.save_version`: 변경 추적 설정과 이전 문서 상태를 확인한 뒤 Version 문서를 저장한다.

**참고할 부분과 선정 이유:** get_diff의 changed/added/removed/row_changed 구조를 참고해 값 수정과 행 추가·삭제를 구별한다. save_version은 저장 전 문서와 현재 문서를 비교할 수 있을 때만 기록하며 track_changes 설정을 확인한다. Version 기록을 대상 문서 종류·ID와 연결하고, 업무 처리자 자체의 기록은 6번의 completed_by 또는 문서 메타데이터와 함께 설계한다.

**함께 볼 파일**

- [frappe/workflow/doctype/workflow_action/workflow_action.py](https://github.com/frappe/frappe/blob/667fbb59e429e45592f02373729188d1c62d2a47/frappe/workflow/doctype/workflow_action/workflow_action.py) — 승인 완료자·역할·시각을 별도로 남기는 예
- [frappe/desk/doctype/todo/todo.py](https://github.com/frappe/frappe/blob/667fbb59e429e45592f02373729188d1c62d2a47/frappe/desk/doctype/todo/todo.py) — 담당자 변경을 사람이 읽는 댓글로 남기는 예

**환경:** Python·JavaScript 기반 Frappe 전체 프레임워크 코드. 이 커밋 pyproject.toml은 Python >=3.14,<3.15와 DB 드라이버·Redis·RQ 등을 요구한다. 개별 함수만 복사해 실행할 수 있는 독립 예제가 아니다.

**한계·별도로 정할 것:** 모든 변경이 무조건 남는 감사 저장소가 아니다. track_changes 비활성화·ignore_version·설치/패치 등의 제외 조건과 무시되는 필드가 있다. 위변조 방지·영구 보존·삭제 추적을 보장하는 증거로 사용하지 않는다.

**확인:** 위 파일 코드 열람 · 2026-10-29 · 실행 **미검증** · [라이선스: MIT](https://github.com/frappe/frappe/blob/667fbb59e429e45592f02373729188d1c62d2a47/LICENSE)

</details>

<a id="ai-guide"></a>

## AI가 이 자료를 사용할 때

사용자용 설명의 예시는 실제 과제에서의 사용 상황을 가정한 것이다. 예제 프로그램에 그 업무가 그대로 구현되어 있다는 뜻은 아니다. 관련 항목의 기술 정보와 아래 원칙을 함께 확인한다.

<details>
<summary>AI용 사용 원칙·확인 범위 펼치기</summary>

## AI가 사용하는 순서

1. `docs/AGREEMENT.md`와 `docs/SPEC.md`에서 합의한 기능을 확인하고 맨 위 목차와 항목별 찾는 말로 관련 항목을 찾는다.
2. 해당 항목의 **먼저 볼 코드·참고할 부분·함께 볼 파일·환경과 한계**를 읽는다. 우선 필요한 핵심 기능 1~2개 항목부터 링크의 코드를 확인한다. 그 구현을 이해하는 데 필요한 연관 파일·환경·라이선스는 추가로 확인하되, 관련 없는 모든 링크를 미리 열지는 않는다. 현재 프로젝트의 언어·구조에 맞는 부분을 고른다.
3. 왜 이 부분을 참고하는지 설명한다. 전체 저장소 설치나 새 라이브러리 도입이 자동으로 필요한 것은 아니다. 참고할 항목이 없거나 맞지 않으면 그 이유를 밝히고 추가 조사는 꼭 필요할 때만 한다.
4. 업무 기준·권한·계산 규칙은 현재 과제의 합의를 따른다. 예제의 기준을 요구사항으로 가져오거나 `SPEC`에 없는 기능을 추가하지 않는다.
5. 원격 소스가 열리지 않으면 같은 실패를 계속 반복하지 않는다. 일시적 오류인지 확인할 가치가 있을 때만 같은 고정 버전의 원문에 한 번 더 접근하고, 계속 실패하면 중단한다. 접근 제한을 우회하거나 확인 없이 다른 버전으로 바꾸지 않는다.
6. 접근할 수 없으면 ‘원본 미열람’으로 표시한다. 항목의 설명·한계와 합의된 요구를 바탕으로 현재 기술에서 독립 구현이 가능한 부분은 진행하고 실제 입력·기대 결과로 검증한다. 확인하지 못한 원본의 동작·호환성을 추정해 보장하지 않는다. 원본과의 연동이나 특정 동작 확인이 꼭 필요하면 미확인 사항과 필요한 자료를 남긴다.
7. 원본을 읽고 적용한 경우도 실제 과제의 입력·기대 결과로 검증한다. 코드 열람·직접 구현·실행 검증을 구분해 보고하며, 이 안내서만 보고 원본을 확인했다고 쓰지 않는다.

## 확인 수준과 읽는 법

- **코드 확인일: 2026-10-29 / 예제 실행: 전부 미검증.** 나열한 소스·연관 파일·설정·라이선스를 읽었으며 참고 프로젝트를 설치하거나 실행하지 않았다.
- 코드 링크는 조사한 **커밋(코드의 특정 저장 시점)** 으로 고정했다. 최신 권장 버전이나 현재 환경에서 작동하는 버전을 보장하는 목록은 아니다.
- **자료 형태**는 완성 앱의 일부인지, 화면 예제인지, 함수들을 조합하는 재료인지 구분한다. 특히 pandas·NumPy 항목은 완성된 업무 프로그램이 아니다.
- 항목의 **먼저 볼 코드**와 **함께 볼 파일**이 실제 열람한 범위다. 의존성 전체와 모든 실행 경로를 검토했다는 뜻은 아니다.
- 라이선스 이름과 확인한 원문을 각 항목에 연결했다. 코드를 옮길 때 해당 조건과 별도 파일 고지를 확인한다. Easy!Appointments는 GPL-3.0이며, 이 안내서가 모든 코드를 같은 조건으로 재사용할 수 있다고 보장하지 않는다.
- 특히 9번 분류의 Easy!Appointments는 우선 동작과 설계 원리를 참고한다. 실제 코드를 가져오려면 출처·커밋·파일 경로를 기록하고, 제출·배포 방식에 따른 라이선스 적용과 소스 제공 등의 조건을 [라이선스 원문](https://github.com/alextselegidis/easyappointments/blob/f6c8a4c2f364bf8c64b1f913a531a7134dcfd3c6/LICENSE)에서 확인한다. 출처 표시만으로 재사용 조건을 충족했다고 보지 않는다.

### 분류별 근거 미확보 범위

#### 4번 분류

**이 분류에서 아직 근거를 확보하지 못한 범위**

- kg↔g·℃↔℉ 등 물리량 단위 자동 인식·차원 검사 완성 예제는 없다. 실제 입력 단위와 변환 규칙에 맞춰 별도 조사한다.

#### 8번 분류

**이 분류에서 아직 근거를 확보하지 못한 범위**

- 문서 원문을 보며 AI 결과를 직접 수정하고 최종 확정하는 완성 화면은 확인하지 않았다. 이 분류는 검색·출처·추출·요약·검사 후 대기 처리까지를 다룬다.

#### 9번 분류

**이 분류에서 아직 근거를 확보하지 못한 범위**

- 동시에 들어온 두 예약 중 하나만 성공하도록 DB 수준에서 강제하는 구현은 이번 참조에서 확인하지 못했다. 실전 요구가 ‘중복 절대 금지’이면 트랜잭션/제약 설계와 동시성 시험을 별도로 해야 한다.

#### 10번 분류

**이 분류에서 아직 근거를 확보하지 못한 범위**

- 완성된 통계/ML 이상 탐지 파이프라인과 알림 센터 화면 예제는 없다. 이동 통계는 판정 재료, Prometheus/Alertmanager는 상태·중복 처리 원리 참고다.

#### 11번 분류

**이 분류에서 아직 근거를 확보하지 못한 범위**

- 특정 사내 시스템과의 실제 연결, 데이터 동기화의 충돌 해결, 중복 없이 한 번만 처리되는 보장은 이 자료에 포함되지 않는다.

## 이 자료를 갱신할 때

새 기능은 사용 장면·정확한 코드·참고할 부분·연관 파일·환경·한계·라이선스·확인일을 함께 적는다. 파일을 직접 확인하지 못했으면 조사 미완료로 표시한다. 실행 여부는 코드 열람과 구분한다. 기준 버전을 바꾸면 관련 코드와 설명을 다시 맞춘다.

</details>
