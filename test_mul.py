from cdc import Calculator


# T-MUL-REAL1
def test_mul_real_numbers():
    calc = Calculator()
    calc.push(3)
    calc.push(-2)
    calc.mul()

    assert calc.stack == [-6]
