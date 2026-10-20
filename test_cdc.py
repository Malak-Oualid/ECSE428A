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
