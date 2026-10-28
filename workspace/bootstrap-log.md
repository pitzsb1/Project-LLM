# P4 초기 구성 기록

작성일: 2026-10-28 (Asia/Seoul). 최종 상태: 초기 환경 준비 완료 — py311 경로 확인 후 Python 3.11.11로 정식 초기 검사 통과. 아래에는 초기 실패와 해결 기록을 순서대로 보존한다.

## 수행 범위
최소 패키지 진입점·TOML 설정 로더·영어 가상 JSON 표본·표준 unittest smoke test·.gitignore·.python-version·requirements.txt를 작성했다. 뉴스 수집·LLM 분석·보고서·화면은 구현하지 않았다. 써드파티 패키지 설치와 API 호출은 하지 않았다. 환경 변수를 사용하지 않으므로 .env.example은 현재 불필요하다.

## 환경 확인
- `command -v python3.11`: 출력 없음, 종료 코드 1. 이후 명령과 묶인 탐색에서 확인.
- `python3 --version`: Python 3.14.4, 종료 코드 0.
- `/Users/pitzsb1/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 --version`: Python 3.12.14, 종료 코드 0. 프로젝트 런타임으로 사용하지 않음.
- 일반적인 Homebrew·Python.framework·pyenv·uv·conda 설치 경로 탐색에서는 3.11을 확인하지 못함. 컴퓨터 전체에 없다고 단정하지 않음.
- Python 3.11을 설치할지 개인에게 질문했고 답변 대기 중. 임의로 프로젝트 버전을 변경하거나 3.14로 .venv를 만들지 않음.

## 실제 진단 실행
작업 폴더: /Users/pitzsb1/Project-LLM. 아래는 3.14 진단이며 정식 3.11 검사 통과가 아니다. 저장 전 임시 폴더에서도 같은 진단을 실행해 같은 결과를 얻었다. 아래는 저장 후 프로젝트 폴더에서 재현한 증거다.

### smoke-diagnostic
명령: `PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v`

종료 코드: 1. 원본 로그: `workspace/logs/smoke-diagnostic.txt` (Git 제외).

```text
test_configured_fixture_is_readable_and_synthetic (test_smoke.HarnessSmokeTests.test_configured_fixture_is_readable_and_synthetic) ... ok
test_declared_python_version (test_smoke.HarnessSmokeTests.test_declared_python_version) ... FAIL
test_offline_json_configuration (test_smoke.HarnessSmokeTests.test_offline_json_configuration) ... ok
test_project_config_loads (test_smoke.HarnessSmokeTests.test_project_config_loads) ... ok

======================================================================
FAIL: test_declared_python_version (test_smoke.HarnessSmokeTests.test_declared_python_version)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/pitzsb1/Project-LLM/tests/test_smoke.py", line 14, in test_declared_python_version
    self.assertEqual(sys.version_info[:2], (3, 11), "Project requires Python 3.11")
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Tuples differ: (3, 14) != (3, 11)

First differing element 1:
14
11

- (3, 14)
?      ^

+ (3, 11)
?      ^
 : Project requires Python 3.11

----------------------------------------------------------------------
Ran 4 tests in 0.001s

FAILED (failures=1)

```

### config-diagnostic
명령: `PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 python3 -m news_crosscheck`

종료 코드: 0. 원본 로그: `workspace/logs/config-diagnostic.txt` (Git 제외).

```text
Harness config loaded: news-crosscheck
API enabled: False
News analysis: not implemented

```

## 판정과 다음 조치
4개 테스트 중 3개 통과, 1개 실패. 실패는 프로젝트가 요구하는 3.11과 실행된 3.14가 다르기 때문이다. 설정·JSON·모듈은 진단에서 로드되었지만 정식 환경 통과는 아니다. 기준은 변경하지 않았다. 수정 재시도 0회(환경 준비가 필요한 상태).
Python 3.11 확보 후 README의 준비 명령으로 .venv를 생성하고 정식 검사를 실행해 이 기록에 새 실행 결과를 추가한다. 실제 API·검색·기사 분석 품질은 미검증이다.

## Python 3.11 경로 확인 후 정식 실행 (2026-10-28)

개인이 py311 커널을 알려줬다. ~/Library/Jupyter/kernels/py311/kernel.json의 argv[0]에서 /opt/anaconda3/envs/py311/bin/python을 확인했다. `--version`은 Python 3.11.11, `-m pip --version`은 pip 26.0.1이며 각각 종료 코드 0이다. 커널 환경은 변경하지 않고 해당 Python으로 프로젝트 .venv를 생성한다.

### venv-create
명령: `/opt/anaconda3/envs/py311/bin/python -m venv .venv`

종료 코드: 0. 원본 로그: `workspace/logs/venv-create.txt` (Git 제외).

```text

```

### venv-version
명령: `.venv/bin/python --version`

종료 코드: 0. 원본 로그: `workspace/logs/venv-version.txt` (Git 제외).

```text
Python 3.11.11

```

### venv-pip
명령: `.venv/bin/python -m pip --version`

종료 코드: 0. 원본 로그: `workspace/logs/venv-pip.txt` (Git 제외).

```text
pip 24.0 from /Users/pitzsb1/Project-LLM/.venv/lib/python3.11/site-packages/pip (python 3.11)

```

### smoke-py311
명령: `PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m unittest discover -s tests -v`

종료 코드: 0. 원본 로그: `workspace/logs/smoke-py311.txt` (Git 제외).

```text
test_configured_fixture_is_readable_and_synthetic (test_smoke.HarnessSmokeTests.test_configured_fixture_is_readable_and_synthetic) ... ok
test_declared_python_version (test_smoke.HarnessSmokeTests.test_declared_python_version) ... ok
test_offline_json_configuration (test_smoke.HarnessSmokeTests.test_offline_json_configuration) ... ok
test_project_config_loads (test_smoke.HarnessSmokeTests.test_project_config_loads) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK

```

### config-py311
명령: `PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m news_crosscheck`

종료 코드: 0. 원본 로그: `workspace/logs/config-py311.txt` (Git 제외).

```text
Harness config loaded: news-crosscheck
API enabled: False
News analysis: not implemented

```

최종 P4 판정: 초기 환경 준비 완료. 프로젝트 .venv는 Python 3.11.11이며 smoke test 4개 통과, 설정 확인 종료 코드 0. 초기 버전 문제는 해결됐다. 앱 기능·기사 분석·실제 API 품질과 스킬 발견/호출은 미검증이다. 추가 코드 수정 0회.
