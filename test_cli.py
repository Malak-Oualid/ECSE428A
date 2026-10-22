import subprocess
import sys

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


# T-ADD-REAL1
def test_cli_add_real():
    assert run("push 2 push 5 add pop") == "7 + j0"


# T-SUB-REAL1
def test_cli_sub_real():
    assert run("push 5 push 2 sub pop") == "3 + j0"


# T-DEL-REAL1
def test_cli_delete_real():
    assert run("push 1 push 2 delete pop") == "1 + j0"


def test_cli_uppercase_commands():
    assert run("PUSH 5 POP") == "5 + j0"


def test_cli_program_prints_result():
    result = subprocess.run([sys.executable, "cdc.py", "push", "5", "pop"],
                            capture_output=True, text=True)
    assert result.stdout == "5 + j0\n"


def test_cli_program_prints_nothing_without_pop():
    result = subprocess.run([sys.executable, "cdc.py", "push", "5"],
                            capture_output=True, text=True)
    assert result.stdout == ""


def test_cli_negative_zero_shown_as_zero():
    assert run("push 0 push -1 mul pop") == "0 + j0"


def test_cli_multiple_pops():
    assert run("push 1 push 2 pop pop") == "2 + j0\n1 + j0"


# Regression tests: remaining rows of the assignment's test table

# T-PUSH-CPLX1
def test_cli_push_complex_compact():
    assert run("push -2.5-j0.25 pop") == "-2.5 - j0.25"


# T-ADD-CPLX1
def test_cli_add_complex():
    assert run("push 3+j4 push 1-j2 add pop") == "4 + j2"


# T-ADD-ERR1
def test_cli_add_underflow():
    assert run("push 3 add") == "Error: stack underflow"


# T-SUB-CPLX1
def test_cli_sub_complex():
    assert run("push 3+j4 push 1-j2 sub pop") == "2 + j6"


# T-SUB-ERR1
def test_cli_sub_underflow():
    assert run("sub") == "Error: stack underflow"


# T-MUL-CPLX1
def test_cli_mul_complex():
    assert run("push 1+j2 push 3-j4 mul pop") == "11 + j2"


# T-MUL-ERR1
def test_cli_mul_underflow():
    assert run("mul") == "Error: stack underflow"


# T-DIV-CPLX1
def test_cli_div_complex():
    assert run("push 4+j2 push 1+j1 div pop") == "3 - j1"


# T-DIV-ERR2
def test_cli_div_by_complex_zero():
    assert run("push 1+j0 push 0+j0 div") == "Error: division by zero"


# T-DEL-CPLX1
def test_cli_delete_complex():
    assert run("push 1+j1 push 2+j3 delete pop") == "1 + j1"


# T-DEL-ERR1
def test_cli_delete_underflow():
    assert run("delete") == "Error: stack underflow"
