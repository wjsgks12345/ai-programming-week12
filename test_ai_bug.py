
import pytest
from find_max import find_max


# 정상 ① 일반적인 정수 리스트
def test_일반적인_리스트():
    assert find_max([3, 8, 2, 5, 1]) == 8


# 정상 ② 첫 번째 값이 최댓값
def test_첫번째_값이_최댓값():
    assert find_max([10, 5, 3, 1]) == 10


# 정상 ③ 마지막 값이 최댓값
def test_마지막_값이_최댓값():
    assert find_max([1, 3, 5, 10]) == 10


# 정상 ④ 중복된 최댓값
def test_중복된_최댓값():
    assert find_max([7, 9, 3, 9]) == 9


# 경계값 ① 원소가 하나인 리스트
def test_원소가_하나():
    assert find_max([5]) == 5


# 경계값 ② 원소가 두 개인 리스트
def test_원소가_두개():
    assert find_max([3, 8]) == 8


# 경계값 ③ 모든 값이 동일
def test_모든_값이_동일():
    assert find_max([4, 4, 4, 4]) == 4


# 경계값 ④ 음수만 존재
def test_음수_리스트():
    assert find_max([-10, -3, -7, -1]) == -1


# 경계값 ⑤ 0이 포함된 리스트
def test_0이_포함된_리스트():
    assert find_max([-5, 0, -2]) == 0


# 예외 ① 빈 리스트
def test_빈_리스트():
    with pytest.raises(IndexError):
        find_max([])


# 예외 ② 숫자와 문자열 혼합
def test_잘못된_자료형():
    with pytest.raises(TypeError):
        find_max([1, "abc", 3])
