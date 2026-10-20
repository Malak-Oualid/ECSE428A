from cdc import Calculator


# T-PUSH-REAL1
def test_pop_real_number():
    calc = Calculator()
    calc.push(5)

    assert calc.pop() == "5 + j0"
