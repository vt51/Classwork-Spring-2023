import pytest


def test_add():
    from add import add
    answer = add(0.1, 0.2)
    assert answer == pytest.approx(0.3)
# default = 1.0e-7 / abs=0.1
