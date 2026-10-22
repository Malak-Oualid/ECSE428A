from cdc import run


# T-PUSH-REAL1
def test_cli_push_real_then_pop():
    assert run("push 5 pop") == "5 + j0"


# T-MUL-REAL1
def test_cli_mul_real():
    assert run("push 3 push -2 mul pop") == "-6 + j0"


# T-PUSH-CPLX2
def test_cli_push_complex_with_spaces():
    assert run("push 3 + j 4 pop") == "3 + j4"


# T-POP-ERR1
def test_cli_pop_empty_stack():
    assert run("pop") == "Error: stack underflow"


# T-DIV-REAL1
def test_cli_div_real():
    assert run("push 8 push 2 div pop") == "4 + j0"


# T-DIV-ERR1
def test_cli_div_by_zero():
    assert run("push 1 push 0 div") == "Error: division by zero"


def test_cli_invalid_token():
    assert run("foo") == "Error: invalid token"


def test_cli_push_invalid_number():
    assert run("push abc pop") == "Error: invalid token"
