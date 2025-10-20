import pytest
from src.calc import add, divide, multiply, sub

def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(5, 3) == 2

def test_mul():
    assert multiply(4, 3) == 12

def test_divide_normal():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
