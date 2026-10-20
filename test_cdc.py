from cdc import Calculator


def test_push_real_number():
    calc = Calculator()
    calc.push(5)

    assert calc.stack == [5]
