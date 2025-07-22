import pytest

@pytest.mark.parametrize("numb, expected", [
    (2, 4),
    (3, 9),
    (4, 16),
    (5, 25)
])


def test_square_check(numb, expected):
    assert numb ** 2 == expected



@pytest.mark.xfail(strict=True)
def test_unexpected_pass():
    assert 1 == 0
