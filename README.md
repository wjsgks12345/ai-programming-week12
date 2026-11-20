# AI 협업 프로그래밍 12주차 - 성적 CSV 검증 프로그램

## ① 무엇을 하나요 (What)

CSV 파일에 저장된 학생들의 성적을 읽고, 유효한 성적과 잘못된 데이터를 구분하는 Python 프로그램입니다.

## ② 왜 만들었나요 (Why)

실제 성적 데이터에는 빈칸, 잘못된 점수, 누락된 정보 등이 포함될 수 있습니다. 이러한 데이터를 올바르게 처리하고 프로그램이 정상적으로 작동하는지 확인하기 위해 제작했습니다. 또한 pytest를 활용하여 정상·예외·경계값 테스트를 수행했습니다.

## ③ 어떻게 쓰나요 (How)

Python 3 환경에서 실행할 수 있습니다.

```bash
python load_scores.py scores.csv
```

실행하면 유효한 성적 목록과 제외된 데이터의 정보가 출력됩니다.

## ④ 어떻게 테스트하나요

먼저 pytest와 pytest-cov를 설치합니다.

```bash
python -m pip install pytest pytest-cov
```

직접 작성한 테스트 실행:

```bash
python -m pytest test_load_scores.py
```

AI 테스트 A 실행:

```bash
python -m pytest test_ai_A.py
```

AI 테스트 B 실행:

```bash
python -m pytest test_ai_B.py
```

코드 커버리지 측정:

```bash
python -m pytest test_load_scores.py --cov=load_scores --cov-report=term-missing
```

테스트 결과:

- 직접 작성: 9 passed, 커버리지 80%
- AI 테스트 A: 10 passed, 커버리지 64%
- AI 테스트 B: 15 passed, 커버리지 80%

## ⑤ 파일 구성

| 파일 | 역할 |
|---|---|
| load_scores.py | 성적 CSV 파일 처리 |
| scores.csv | 일반 성적 데이터 |
| empty.csv | 헤더만 있는 CSV 데이터 |
| weird.csv | 예외 상황이 포함된 CSV 데이터 |
| bug3_logic.py | 버그가 포함된 실습 코드 |
| find_max.py | 함정 테스트를 위한 함수 연결 |
| test_load_scores.py | 직접 작성한 pytest 테스트 |
| test_ai_A.py | 코드를 제공해 AI가 생성한 테스트 |
| test_ai_B.py | 명세서를 제공해 AI가 생성한 테스트 |
| test_ai_bug.py | 버그 탐지 함정 테스트 |

## ⑥ 만든 사람 · AI를 어디에 썼는지

- 만든 사람: 강전한 (2026100721)
- AI를 쓴 곳: 테스트 코드 생성, 테스트 설계 및 비교 분석, README 문서 작성
- 내가 직접 판단한 것: 테스트 실행 결과 확인, 커버리지 비교, 버그 발생 원인 확인 및 최종 결과 검토

## 라이선스

MIT License (LICENSE 파일 참고)
