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
