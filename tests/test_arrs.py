from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 0, 1) == []
    assert arrs.my_slice([], 0, -1) == []
    assert arrs.my_slice([1, 2, 3, 4, 5, 6, 7], 0, 0) == []
    assert arrs.my_slice([1, 2, 3, 4, 5, 6, 7], 7, None) == []
    assert arrs.my_slice([1, 2, 3, 4, 5, 6, 7], 0, 0) == []
    assert arrs.my_slice([1, 2, 3, 4, 5, 6, 7], -2, None) == [6, 7]
    assert arrs.my_slice([1, 2, 3, 4, 5, 6, 7], -5, -2) == [3, 4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5, 6, 7], 0, -2) == [1, 2, 3, 4, 5]
    assert arrs.my_slice([], None, None) == []
    assert arrs.my_slice([-1], -2, None) == [-1]
