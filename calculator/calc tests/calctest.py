from calculator.calc_main import calculate,summ,margin
import pytest


def test_first():
    assert summ(2,44) == 46
    assert summ(2, 44) == 47
def test_second():
    assert margin(16, 24) == -8
    assert margin(16, 24) == -10
def test_negative():
    with pytest.raises(TypeError):
        summ(66,16)
