import pytest
from calculator import Calculator


test_data = [(10, 12), (-5, -7)]   # can be inserted from excel/csv file...


@pytest.mark.usefixtures("calc")
def calc():
    return Calculator()


@pytest.mark.parametrize("a, b", test_data)
def test_calc_sum(calc, a, b):
    assert calc.Sum(a, b) == a+b


@pytest.mark.parametrize("a, b", test_data)
def test_calc_del(calc, a, b):
    assert calc.Del(a, b) == a-b


@pytest.mark.parametrize("a, b", test_data)
def test_calc_mul(calc, a, b):
    assert calc.Multiple(a, b) == a*b


@pytest.mark.parametrize("a, b", test_data)
def test_calc_div(calc, a, b):
    assert calc.Div(a, b) == a/b


