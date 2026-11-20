
import csv
import pytest
from load_scores import load_scores


# 정상 ① 일반 파일
def test_정상_파일을_읽는다():
    kept, skipped = load_scores("scores.csv")
    assert len(kept) == 5


# 정상 ② 빈 줄
def test_빈_줄은_건너뛴다(tmp_path):
    path = tmp_path / "blank.csv"
    path.write_text("이름,점수\n김하나,80\n\n이철수,90\n", encoding="utf-8")
    kept, skipped = load_scores(path)
    assert kept == [("김하나", 80), ("이철수", 90)]
    assert skipped == []


# 정상 ③ 이름에 쉼표
def test_이름에_쉼표가_있어도_읽는다(tmp_path):
    path = tmp_path / "comma.csv"
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["이름", "점수"])
        writer.writerow(["김,하나", 85])

    kept, skipped = load_scores(path)
    assert kept == [("김,하나", 85)]


# 예외 ① 파일 없음
def test_없는_파일이면_오류가_난다():
    with pytest.raises(FileNotFoundError):
        load_scores("없는파일.csv")


# 예외 ② 헤더만 있음
def test_헤더만_있으면_빈_결과이다():
    kept, skipped = load_scores("empty.csv")
    assert kept == []
    assert skipped == []


# 경계 ①②③
@pytest.mark.parametrize("score,valid", [
    (0, True),
    (100, True),
    (101, False),
])
def test_점수_경계값(tmp_path, score, valid):
    path = tmp_path / "boundary.csv"
    path.write_text(f"이름,점수\n김하나,{score}\n", encoding="utf-8")

    kept, skipped = load_scores(path)
    assert (len(kept) == 1) == valid

def test_이름이_비어있으면_건너뛴다(tmp_path):
    path = tmp_path / "no_name.csv"
    path.write_text("이름,점수\n,80\n", encoding="utf-8")

    kept, skipped = load_scores(path)

    assert kept == []
    assert len(skipped) == 1
    assert skipped[0][2] == "이름이 비어 있음"
