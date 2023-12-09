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
        assert cl.multiply(2, "a") == 2


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

def test_positive_sqare():
    """
        scenario: summ nm a sqrt nm b in different variants
        :return: Test result
        """
    assert cl.square(4) == 2
    assert cl.square(16) == 4
    with pytest.raises(TypeError):
        assert cl.square("*") == 2

@pytest.mark.xfail(raises=TypeError)  # decorator
def test_negative_square():
    assert cl.square(2) != 4
    assert cl.square(2) != 0
    cl.square( "+")

def test_positive_power():
    """
        scenario: summ nm a power to nm b in different variants
        :return: Test result
        """
    assert cl.power(2, 2) == 4
    assert cl.power(2, -2) == 0.25
    with pytest.raises(TypeError):
        assert cl.power(2, "") == 2


@pytest.mark.xfail(raises=TypeError)  # decorator
def test_negative_power():
    assert cl.power(2, 1) != 4
    assert cl.power(2, -9) != 0
    cl.power(0, "+")