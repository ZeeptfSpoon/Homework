from calculator import calc_main as cl
import pytest


def test_positive_summ():
    """
    scenario: summ nm a+ nm b in different variants
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


# def test_negative():
