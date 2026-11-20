
import csv
import pytest
from load_scores import load_scores


# ① 정상: 유효한 성적 데이터
def test_정상_데이터(tmp_path):
    path = tmp_path / "scores.csv"
    path.write_text(
        "이름,점수\n김하나,80\n이철수,90\n",
        encoding="utf-8"
    )

    kept, skipped = load_scores(path)

    assert kept == [("김하나", 80), ("이철수", 90)]
    assert skipped == []


# ② 정상: 이름 앞뒤 공백 제거
def test_이름_공백_제거(tmp_path):
    path = tmp_path / "scores.csv"
    path.write_text(
        "이름,점수\n  김하나  ,80\n",
        encoding="utf-8"
    )

    kept, skipped = load_scores(path)

    assert kept == [("김하나", 80)]
    assert skipped == []


# ③ 정상: 동명이인 유지
def test_중복_이름_유지(tmp_path):
    path = tmp_path / "scores.csv"
    path.write_text(
        "이름,점수\n김하나,80\n김하나,90\n",
        encoding="utf-8"
    )

    kept, skipped = load_scores(path)

    assert kept == [("김하나", 80), ("김하나", 90)]
    assert skipped == []


# ④ 정상: 이름에 쉼표 포함
def test_이름에_쉼표(tmp_path):
    path = tmp_path / "scores.csv"

    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["이름", "점수"])
        writer.writerow(["김,하나", 85])

    kept, skipped = load_scores(path)

    assert kept == [("김,하나", 85)]
    assert skipped == []


# ⑤ 예외: 파일이 존재하지 않음
def test_파일_없음(tmp_path):
    path = tmp_path / "missing.csv"

    with pytest.raises(FileNotFoundError):
        load_scores(path)


# ⑥ 예외: 헤더만 존재
def test_헤더만_있는_파일(tmp_path):
    path = tmp_path / "scores.csv"
    path.write_text("이름,점수\n", encoding="utf-8")

    kept, skipped = load_scores(path)

    assert kept == []
    assert skipped == []


# ⑦ 예외: 빈 줄 건너뛰기
def test_빈_줄_건너뛰기(tmp_path):
    path = tmp_path / "scores.csv"
    path.write_text(
        "이름,점수\n김하나,80\n\n이철수,90\n",
        encoding="utf-8"
    )

    kept, skipped = load_scores(path)

    assert kept == [("김하나", 80), ("이철수", 90)]
    assert skipped == []


# ⑧ 예외: 열 개수가 2개가 아님
def test_열_개수_오류(tmp_path):
    path = tmp_path / "scores.csv"
    path.write_text(
        "이름,점수\n김하나,80,추가\n이철수\n",
        encoding="utf-8"
    )

    kept, skipped = load_scores(path)

    assert kept == []
    assert len(skipped) == 2
    assert [row[0] for row in skipped] == [2, 3]


# ⑨ 예외: 이름 또는 점수가 비어 있음
def test_빈_이름과_점수(tmp_path):
    path = tmp_path / "scores.csv"
    path.write_text(
        "이름,점수\n,80\n김하나,\n",
        encoding="utf-8"
    )

    kept, skipped = load_scores(path)

    assert kept == []
    assert len(skipped) == 2
    assert [row[0] for row in skipped] == [2, 3]


# ⑩ 예외: 점수가 정수가 아님
def test_정수가_아닌_점수(tmp_path):
    path = tmp_path / "scores.csv"
    path.write_text(
        "이름,점수\n김하나,85.5\n이철수,abc\n",
        encoding="utf-8"
    )

    kept, skipped = load_scores(path)

    assert kept == []
    assert len(skipped) == 2
    assert [row[0] for row in skipped] == [2, 3]


# ⑪ 경계값: 0점과 100점 허용
@pytest.mark.parametrize("score", [0, 100])
def test_점수_경계값_허용(tmp_path, score):
    path = tmp_path / "scores.csv"
    path.write_text(
        f"이름,점수\n김하나,{score}\n",
        encoding="utf-8"
    )

    kept, skipped = load_scores(path)

    assert kept == [("김하나", score)]
    assert skipped == []


# ⑫ 경계값: 범위를 벗어난 점수 제외
@pytest.mark.parametrize("score", [-1, 101])
def test_점수_범위_초과(tmp_path, score):
    path = tmp_path / "scores.csv"
    path.write_text(
        f"이름,점수\n김하나,{score}\n",
        encoding="utf-8"
    )

    kept, skipped = load_scores(path)

    assert kept == []
    assert len(skipped) == 1
    assert skipped[0][0] == 2


# ⑬ 정상과 잘못된 데이터가 섞인 경우
def test_혼합_데이터(tmp_path):
    path = tmp_path / "scores.csv"
    path.write_text(
        "이름,점수\n"
        "김하나,80\n"
        "이철수,abc\n"
        "박민수,100\n"
        "최영희,-5\n",
        encoding="utf-8"
    )

    kept, skipped = load_scores(path)

    assert kept == [("김하나", 80), ("박민수", 100)]
    assert len(skipped) == 2
    assert [row[0] for row in skipped] == [3, 5]
