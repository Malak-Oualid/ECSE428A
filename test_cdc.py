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
