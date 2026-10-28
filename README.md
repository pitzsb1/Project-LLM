# 다국가·다언론 뉴스 교차검증 에이전트

중동 전쟁 사건에 관한 여러 국가·언론의 보도를 비교해 관점, 공통 정보, 출처별 주장, 불일치와 추가 확인 항목을 근거와 함께 제공하는 프로젝트다.

## 현재 상태
P5: 초기 환경 구성 및 정식 검사 완료. 2026-10-28 `project-check` 명시 호출로 초기 테스트 4개와 설정 확인을 재통과했다([실행 2](workspace/checks.md#등록된-초기-검사--실행-2)). 이번 대화에서 `project-check`·`project-docs`를 명시 호출해 수행했으며 `project-plan` 호출과 개인 회고·최종 채택은 미확인이다. py311 커널의 Python 3.11.11로 프로젝트 .venv를 생성했다. 기본 python3(3.14.4) 대신 .venv/bin/python을 사용한다. 앱·검색·LLM·화면은 미구현이다.

## 준비
이 컴퓨터에서 확인한 Python 3.11 경로는 `/opt/anaconda3/envs/py311/bin/python`이다. 커널 환경 자체는 변경하지 않았다. 다른 컴퓨터에서는 같은 3.11 실행 파일 경로로 바꾼다. 프로젝트 루트에서 실제 확인한 준비 명령:

```bash
/opt/anaconda3/envs/py311/bin/python --version
/opt/anaconda3/envs/py311/bin/python -m venv .venv
.venv/bin/python --version
.venv/bin/python -m pip --version
```
현재 외부 패키지가 없어 설치 명령은 필요 없다. `requirements.txt`에 이를 표시했다. .venv 및 로컬 런타임은 Git에서 제외한다.

## 검사
실제 통과한 검사 명령:

```bash
PYTHONPATH=src .venv/bin/python -m unittest discover -s tests -v
PYTHONPATH=src .venv/bin/python -m news_crosscheck
```
기대 결과와 검사 범위는 [testing](docs/testing.md)을 따른다. 두 번째 명령은 설정 확인용이며 뉴스 분석 앱이 아니다. 정식 3.11 검사에서 테스트 4개 통과, 설정 확인 종료 코드 0을 확인했다. 이전 3.14 진단 실패와 해결 기록은 [실제 실행 기록](workspace/bootstrap-log.md)에 남겼다.
외부 API·키·네트워크를 사용하지 않는다. 초기 데이터는 영어 가상 기사이며 실제 뉴스를 검증하지 않는다. 앱 실행 명령은 기능 구현 후 추가한다.

## 문서별 기준 정보
| 문서 | 기준 정보 | 갱신 시점 |
|---|---|---|
| [proposal.md](proposal.md) | 프로젝트 원래 목표와 기술 계획 | 개인이 목표 변경을 확정할 때 |
| [AGENTS.md](AGENTS.md) | AI가 반복 참고할 작업 규칙·수정 범위 | 규칙 변경 시 |
| [project-brief](docs/project-brief.md) | 제안서 해석·범위·현재 상태 | 범위/상태 변화 시 |
| [open-questions](docs/open-questions.md) | P1 질문과 실제 개인 답변 | 답변·보류 상태 변화 시 |
| [workflow](docs/workflow.md) | 개인·작성자·검사자·검토자 책임과 흐름 | 작업 절차 변경 시 |
| [decisions](docs/decisions/README.md) | 중요 결정 기준과 확정/보류 근거 | 중요 선택 시 |
| [testing](docs/testing.md) | 검사 대상·명령·판정 및 향후 전략 | 환경/테스트 변경 시 |
| [스킬 파일](.agents/skills/) | 반복 계획·검사·문서화 절차 | 절차 변경 시 |
| [workspace 기록](workspace/) | 실제 작업·검사·리뷰 증거 | 작업 수행 시 |

이 README는 탐색과 재현 명령의 진입점이다. 상세 규칙·검사·결정은 각 기준 문서에서 관리하며 중복 복사하지 않는다. `llm-proposal.md`, 참고 보고서, NeuS.pdf는 원자료로 보존한다.

## P5 결과와 남은 확인
[계획](workspace/plan.md) · [검사](workspace/checks.md) · [문서 갱신](workspace/docs-update.md) · [최종 점검](workspace/harness-review.md) · [개인 회고 양식](workspace/reflection.md).
이전 P5는 파일 직접 읽기 수행이었다. 이후 이번 대화에서 `$project-check`·`$project-docs` 명시 호출과 지침 제공을 받아 검사·문서화 산출물을 기록했다([스킬별 상태](docs/skill-status.md)). `$project-plan`의 명시 호출은 미확인이므로 다음 확인 대상으로 남긴다. 명시 호출 수행이 모든 세션의 자동 발견을 보장하지는 않는다.
개인은 회고 양식을 자기 말로 작성하고 결과를 최종 채택한다. 앱 기능 구현은 후속 요청으로 진행한다.
