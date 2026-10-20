from cdc import run


# T-PUSH-REAL1
def test_cli_push_real_then_pop():
    assert run("push 5 pop") == "5 + j0"
