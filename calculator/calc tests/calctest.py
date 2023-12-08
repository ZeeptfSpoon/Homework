from calculator import calc_main as cl
import pytest


def test_positive_summ():
    """
    scenario: summ nm a + nm b in different variants
    :return: Test result
    """
    assert cl.summ(2, 2) == 4
    assert cl.summ(2, -2) == 0
    with pytest.raises(TypeError):
        assert cl.summ(2, "") == 2


@pytest.mark.xfail(raises=TypeError)  # decorator
def test_negative_summ():
    assert cl.summ(2, 1) != 4
    assert cl.summ(2, -9) != 0
    cl.summ(0, "+")

def test_positive_margin():
    """
    scenario: summ nm a - nm b in different variants
    :return: Test result
    """
    assert cl.margin(2, 2) == 0
    assert cl.margin(2, -2) == 4
    with pytest.raises(TypeError):
        assert cl.margin(2, "") == 2


@pytest.mark.xfail(raises=TypeError)  # decorator
def test_negative_margin():
    assert cl.margin(2, 1) != 4
    assert cl.margin(2, -9) != 0
    cl.margin(0, "+")

def test_positive_multiply():
    """
    scenario: summ nm a * nm b in different variants
    :return: Test result
    """
    assert cl.multiply(2, 2) == 4
    assert cl.multiply(2, -2) == -4
    with pytest.raises(TypeError):
        assert cl.multiply(2, "") == 2


@pytest.mark.xfail(raises=TypeError)  # decorator
def test_negative_multiply():
    assert cl.multiply(2, 1) != 4
    assert cl.multiply(2, -9) != 0
    cl.multiply(0, "+")

def test_positive_divide():
    """
        scenario: summ nm a / nm b in different variants
        :return: Test result
        """
    assert cl.divide(2, 2) == 1
    assert cl.divide(2, -2) == -1
    with pytest.raises(TypeError):
        assert cl.divide(2, "") == 2


@pytest.mark.xfail(raises=TypeError)  # decorator
def test_negative_divide():
    assert cl.divide(2, 1) != 4
    assert cl.divide(2, -9) != 0
    cl.divide(0, "+")

def test_positive_divide():
    """
        scenario: summ nm a / nm b in different variants
        :return: Test result
        """
    assert cl.divide(2, 2) == 1
    assert cl.divide(2, -2) == -1
    with pytest.raises(TypeError):
        assert cl.divide(2, "") == 2

@pytest.mark.xfail(raises=TypeError)  # decorator
def test_negative_divide():
    assert cl.divide(2, 1) != 4
    assert cl.divide(2, -9) != 0
    cl.divide(0, "+")