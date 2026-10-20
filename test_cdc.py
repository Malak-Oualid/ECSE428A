from cdc import Calculator


def test_push_real_number():
    calc = Calculator()
    calc.push(5)

    assert calc.stack == [5]


def test_add_real_numbers():
    calc = Calculator()
    calc.push(2)
    calc.push(5)
    calc.add()

    assert calc.stack == [7]


def test_add_complex_numbers():
    calc = Calculator()
    calc.push("3+j4")
    calc.push("1-j2")
    calc.add()

    assert calc.stack == [4 + 2j]


def test_sub_real_numbers():
    calc = Calculator()
    calc.push(5)
    calc.push(2)
    calc.sub()

    assert calc.stack == [3]


def test_sub_complex_numbers():
    calc = Calculator()
    calc.push("3+j4")
    calc.push("1-j2")
    calc.sub()

    assert calc.stack == [2 + 6j]


import pytest


def test_sub_stack_underflow():
    calc = Calculator()
    calc.push(3)

    with pytest.raises(ValueError, match="stack underflow"):
        calc.sub()

def test_delete_real_number():
    calc = Calculator()
    calc.push(1)
    calc.push(2)
    calc.delete()

    assert calc.stack == [1]

def test_delete_complex_number():
    calc = Calculator()
    calc.push("1+j1")
    calc.push("2+j3")
    calc.delete()

    assert calc.stack == [1 + 1j]


def test_delete_stack_underflow():
    calc = Calculator()

    with pytest.raises(ValueError, match="stack underflow"):
        calc.delete()


def test_add_stack_underflow():
    calc = Calculator()
    calc.push(3)

    with pytest.raises(ValueError, match="stack underflow"):
        calc.add()


def test_push_pure_imaginary():
    calc = Calculator()
    calc.push("j5")

    assert calc.stack == [5j]
