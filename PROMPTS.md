# Prompt log

ECSE 428, Assignment A: complex `dc` calculator (`cdc`).

Generative AI was used following the Kent Beck TDD cycle: one prompt for just enough test to fail, then, after the test was seen failing, one prompt for just enough code to pass. Each prompt was proposed by the AI assistant and reviewed and approved before any test or code was generated from it. The full test suite was run after every change. Step numbers match the slides.

## Malak Oualid

### Step 1: MUL: multiply two real numbers (T-MUL-REAL1)

- **Test prompt:** Write a pytest test for T-MUL-REAL1 in test_mul.py: push 3 and -2 onto a Calculator, call mul(), and the stack should be [-6]. Write only the test, no production code.
- **Code prompt:** Add the smallest mul method to Calculator in cdc.py that makes T-MUL-REAL1 pass without breaking existing tests.
- **Commit:** `edaca83`

### Step 2: POP: real number in canonical form (T-PUSH-REAL1 (pop half))

- **Test prompt:** Write a pytest test in test_pop.py: after Calculator().push(5), calc.pop() should return "5 + j0". Write only the test, no production code.
- **Code prompt:** Add the smallest pop method to Calculator in cdc.py that makes this test pass without breaking existing tests.
- **Commit:** `c257ef2`

### Step 3: POP: format a complex number (Canonical output)

- **Test prompt:** Add a pytest test to test_pop.py: after Calculator().push(3-1j), calc.pop() should return "3 - j1". Write only the test, no production code.
- **Code prompt:** Change pop in cdc.py with the smallest change that formats the value as "RVAL ± jIMAG" so this test passes without breaking existing tests.
- **Commit:** `37044f8`

### Step 4: PARSE: complex number text (T-PUSH-CPLX1 (parsing))

- **Test prompt:** Write a pytest test in test_parse.py: parse_number("3+j4") from cdc should return the complex number 3+4j. Write only the test, no production code.
- **Code prompt:** Add the smallest parse_number(text) function to cdc.py that makes this test pass without breaking existing tests.
- **Commit:** `647685f`

### Step 5: PARSE: real number text (T-PUSH-REAL1 (parsing))

- **Test prompt:** Add a pytest test to test_parse.py: parse_number("5") should return 5. Write only the test, no production code.
- **Code prompt:** Change parse_number in cdc.py with the smallest change that makes this test pass without breaking existing tests.
- **Commit:** `13f8d2c`

### Step 6: PARSE: complex number with spaces (T-PUSH-CPLX2 (parsing))

- **Test prompt:** Add a pytest test to test_parse.py: parse_number("3 + j 4") should return 3+4j. Write only the test, no production code.
- **Code prompt:** Change parse_number in cdc.py with the smallest change that makes this test pass without breaking existing tests.
- **Commit:** `cfb568a`

### Step 7: CLI: push then pop (T-PUSH-REAL1)

- **Test prompt:** Write a pytest test in test_cli.py: run("push 5 pop") from cdc should return "5 + j0". Write only the test, no production code.
- **Code prompt:** Add the smallest run(text) function to cdc.py that makes this test pass by using Calculator and parse_number, without breaking existing tests.
- **Commit:** `2555c48`

### Step 8: CLI: a sequence of commands (T-MUL-REAL1)

- **Test prompt:** Add a pytest test to test_cli.py: run("push 3 push -2 mul pop") should return "-6 + j0". Write only the test, no production code.
- **Code prompt:** Change run in cdc.py with the smallest change that loops over the tokens and handles push, mul and pop, so this test passes without breaking existing tests.
- **Commit:** `610f963`

### Step 9: CLI: push a spaced complex number (T-PUSH-CPLX2)

- **Test prompt:** Add a pytest test to test_cli.py: run("push 3 + j 4 pop") should return "3 + j4". Write only the test, no production code.
- **Code prompt:** Change run in cdc.py with the smallest change so that after push it collects all following tokens up to the next command keyword and parses them together, so this test passes without breaking existing tests.
- **Commit:** `fc1bd56`

### Step 10: CLI: pop on an empty stack (T-POP-ERR1)

- **Test prompt:** Add a pytest test to test_cli.py: run("pop") should return "Error: stack underflow". Write only the test, no production code.
- **Code prompt:** Change run in cdc.py with the smallest change that catches the IndexError from an empty stack and returns "Error: stack underflow", so this test passes without breaking existing tests.
- **Commit:** `fc42b9b`

### Step 11: DIV: divide two real numbers (T-DIV-REAL1)

- **Test prompt:** Add a pytest test to test_cli.py: run("push 8 push 2 div pop") should return "4 + j0". Write only the test, no production code.
- **Code prompt:** Add the smallest change to cdc.py that makes this test pass: a div method on Calculator, div added to the command keywords, and run calling it, without breaking existing tests.
- **Commit:** `b3fe5d7`

### Step 12: DIV: division by zero (T-DIV-ERR1)

- **Test prompt:** Add a pytest test to test_cli.py: run("push 1 push 0 div") should return "Error: division by zero". Write only the test, no production code.
- **Code prompt:** Change run in cdc.py with the smallest change that catches ZeroDivisionError and returns "Error: division by zero", so this test passes without breaking existing tests.
- **Commit:** `1660379`

### Step 13: Invalid token: unknown command (Invalid token)

- **Test prompt:** Add a pytest test to test_cli.py: run("foo") should return "Error: invalid token". Write only the test, no production code.
- **Code prompt:** Change run in cdc.py with the smallest change that raises ValueError("Error: invalid token") for any unknown token and returns the message of any ValueError, so this test passes without breaking existing tests.
- **Commit:** `c9bfd4e`

### Step 14: Invalid token: bad number after push (Invalid token)

- **Test prompt:** Add a pytest test to test_cli.py: run("push abc pop") should return "Error: invalid token". Write only the test, no production code.
- **Code prompt:** Change parse_number in cdc.py with the smallest change that raises ValueError("Error: invalid token") when the text isn't a valid number, so this test passes without breaking existing tests.
- **Commit:** `ac6f0e1`

### Step 15: Refactor: one parser (Refactor (no new test))

- **Refactor prompt:** Refactor push in cdc.py to use parse_number for string input and remove the duplicate parsing code. All existing tests must still pass.
- **Commit:** `dc551f2`

### Step 16: CLI: add (T-ADD-REAL1)

- **Test prompt:** Add a pytest test to test_cli.py: run("push 2 push 5 add pop") should return "7 + j0". Write only the test, no production code.
- **Code prompt:** Change run in cdc.py with the smallest change that recognises add as a command and calls calc.add(), so this test passes without breaking existing tests.
- **Commit:** `32bccce`

### Step 17: CLI: sub (T-SUB-REAL1)

- **Test prompt:** Add a pytest test to test_cli.py: run("push 5 push 2 sub pop") should return "3 + j0". Write only the test, no production code.
- **Code prompt:** Change run in cdc.py with the smallest change that recognises sub as a command and calls calc.sub(), so this test passes without breaking existing tests.
- **Commit:** `0bad841`

### Step 18: CLI: delete (T-DEL-REAL1)

- **Test prompt:** Add a pytest test to test_cli.py: run("push 1 push 2 delete pop") should return "1 + j0". Write only the test, no production code.
- **Code prompt:** Change run in cdc.py with the smallest change that recognises delete as a command and calls calc.delete(), so this test passes without breaking existing tests.
- **Commit:** `7d026dd`

### Step 19: Case-insensitive commands (Appendix B)

- **Test prompt:** Add a pytest test to test_cli.py: run("PUSH 5 POP") should return "5 + j0". Write only the test, no production code.
- **Code prompt:** Change run in cdc.py with the smallest change that makes command keywords case-insensitive, so this test passes without breaking existing tests.
- **Commit:** `cf9c64a`

### Step 20: Command-line entry point (CLI program)

- **Test prompt:** Add a pytest test to test_cli.py that runs python cdc.py push 5 pop as a subprocess and checks that it prints "5 + j0". Write only the test, no production code.
- **Code prompt:** Add the smallest entry point to cdc.py so that running python cdc.py <commands> prints the result of run on the joined arguments, so this test passes without breaking existing tests.
- **Commit:** `7f775c3`

### Step 21: No output without pop (CLI program)

- **Test prompt:** Add a pytest test to test_cli.py that runs python cdc.py push 5 as a subprocess and checks that it prints nothing. Write only the test, no production code.
- **Code prompt:** Change the entry point in cdc.py with the smallest change so it prints nothing when run has no result, so this test passes without breaking existing tests.
- **Commit:** `005c906`

### Step 22: Negative zero shown as 0 (Canonical output)

- **Test prompt:** Add a pytest test to test_cli.py: run("push 0 push -1 mul pop") should return "0 + j0" (negative zero shown as 0). Write only the test, no production code.
- **Code prompt:** Change pop in cdc.py with the smallest change that shows a negative-zero real part as 0, so this test passes without breaking existing tests.
- **Commit:** `5d054f1`

### Step 23: Several pops in one line (POP)

- **Test prompt:** Add a pytest test to test_cli.py: run("push 1 push 2 pop pop") should return "2 + j0\n1 + j0" (each pop on its own line). Write only the test, no production code.
- **Code prompt:** Change run in cdc.py with the smallest change so that every pop adds its result to the output and run returns all results joined by newlines, so this test passes without breaking existing tests.
- **Commit:** `91020cb`

### Step 24: Regression: the rest of the assignment table (11 table rows)

- **Test prompt:** Add regression tests to test_cli.py for every row of the assignment's test table that isn't already covered at the command-line level, using the exact input and expected output from the table.
- **Commit:** `e434c78`

## Alexandre Danon

### Step 1: PUSH — store a real number

- **Test prompt:** Write the first pytest test in `test_cdc.py`: create `Calculator`, call `push(5)`, and verify `calc.stack == [5]`. Write the test before implementing `Calculator`.
- **Observed RED:** Importing `Calculator` failed because the class did not yet exist.
- **Code prompt:** Implement only the `Calculator` class, its initially empty stack and the `push(value)` method in `cdc.py` to pass the test.
- **Observed GREEN:** 1 test passed.

### Step 2: ADD — two real numbers (T-ADD-REAL1)

- **Test prompt:** Add `test_add_real_numbers`: push `2` and `5`, call `add()`, and assert that the stack contains `[7]`. Do not implement `add()` yet.
- **Observed RED:** `AttributeError` because `Calculator` had no `add` method; the existing PUSH test passed.
- **Code prompt:** Add the smallest `add()` method: pop both operands in stack order and push their sum.
- **Observed GREEN:** 2 tests passed.

### Step 3: ADD — two complex numbers (T-ADD-CPLX1)

- **Test prompt:** Test `push("3+j4")`, `push("1-j2")`, and `add()`; expect `[4 + 2j]`.
- **Observed RED:** Strings were concatenated instead of added numerically.
- **Code prompt:** Extend `push()` to convert textual `a+jb` and `a-jb` numbers to Python complex numbers while preserving the existing tests.
- **Observed GREEN:** 3 tests passed.

### Step 4: SUB — two real numbers (T-SUB-REAL1)

- **Test prompt:** Add a pytest test that pushes `5` and `2`, calls `sub()`, and expects `[3]`.
- **Observed RED:** `AttributeError` because `sub()` did not exist.
- **Code prompt:** Add `sub()` by popping `b` then `a` and pushing `a - b`; do not modify existing tests.
- **Observed GREEN:** 4 tests passed.

### Step 5: SUB — two complex numbers (T-SUB-CPLX1)

- **Test prompt:** Add a test for `(3+j4) - (1-j2)`, expecting `[2 + 6j]`.
- **Result:** The test **passed immediately** because the prior number parser and subtraction method already supported this case. No production code change was needed; 5 tests passed. This was a regression/coverage test, not a new RED–GREEN implementation cycle.

### Step 6: SUB — insufficient operands (T-SUB-ERR1)

- **Test prompt:** Push only `3`, call `sub()`, and assert that it raises `ValueError` with text `stack underflow`.
- **Observed RED:** Python raised `IndexError: pop from empty list` instead.
- **Code prompt:** Add a stack-length check to `sub()` that raises `ValueError("Error: stack underflow")` before changing the stack.
- **Observed GREEN:** 6 tests passed.

### Step 7: SUB — refactor duplicate definition

- **Refactor prompt:** Remove the older duplicate `sub()` definition, leaving only the version that validates stack length.
- **Regression result:** All 6 existing tests still passed. No new test was required for this cleanup.

### Step 8: DELETE — real numbers (T-DEL-REAL1)

- **Test prompt:** Push `1` and `2`, call `delete()`, and assert that the remaining stack is `[1]`.
- **Observed RED:** `AttributeError` because `delete()` did not exist.
- **Code prompt:** Implement the smallest `delete()` method that removes the top stack element without printing it.
- **Observed GREEN:** 7 tests passed.

### Step 9: DELETE — complex numbers (T-DEL-CPLX1)

- **Test prompt:** Push `"1+j1"` and `"2+j3"`, call `delete()`, and assert that the stack contains `[1 + 1j]`.
- **Result:** The test **passed immediately**; `delete()` already worked regardless of the stored number type. 8 tests passed. No new implementation was needed.

### Step 10: DELETE — empty stack (T-DEL-ERR1)

- **Test prompt:** Call `delete()` on an empty `Calculator` and expect `ValueError` matching `stack underflow`.
- **Observed RED:** `IndexError: pop from empty list`.
- **Code prompt:** Check whether the stack is empty before deleting and raise `ValueError("Error: stack underflow")`.
- **Observed GREEN:** 9 tests passed.

### Step 11: ADD — insufficient operands (T-ADD-ERR1)

- **Test prompt:** Push only `3`, call `add()`, and assert that a `ValueError` with `stack underflow` is raised.
- **Observed RED:** `IndexError: pop from empty list`.
- **Code prompt:** Add the same two-operand stack-length validation to `add()` without altering its arithmetic behavior.
- **Observed GREEN:** 10 tests passed.
- **Refactor prompt:** Remove the superseded duplicate `add()` definition and rerun all tests.

### Step 12: PUSH — positive imaginary-only number

- **Test prompt:** Add a test that pushes the text `"j5"` and expects `[5j]`.
- **Observed RED:** The parser stored the string `"5"` rather than a complex value.
- **Code prompt:** Extend `push()` to recognize an initial `j` and convert its following numeric part to a purely imaginary complex number, while preserving the other formats.
- **Observed GREEN:** 11 tests passed.

### Step 13: PUSH — negative real and imaginary parts (T-PUSH-CPLX1)

- **Test prompt:** Add a test that pushes `"-2.5-j0.25"` and expects `[-2.5 - 0.25j]`.
- **Result:** The test **passed immediately** because the existing converter handled this case. 12 tests passed; no production change was made.

### Step 14: PUSH — complex number with spaces (T-PUSH-CPLX2)

- **Test prompt:** Add a test that pushes `"3 + j 4"` and expects `[3 + 4j]`.
- **Result:** The test **passed immediately** with the existing `push()` implementation. 13 tests passed; no production change was made.

### Step 15: PUSH — real number supplied as text

- **Test prompt:** Add a test for `push("-2.5")`, expecting the numeric stack value `[-2.5]`, not the text string.
- **Observed RED:** The stack held `"-2.5"`.
- **Code prompt:** Extend `push()` to call `float(value)` for real strings that do not represent a general complex number.
- **Observed GREEN:** 14 tests passed.

### Step 16: PUSH — negative imaginary-only number

- **Test prompt:** Add a test that pushes `"-j2"` and expects `[-2j]`.
- **Observed RED:** The parser produced the real number `-2.0`.
- **Code prompt:** Add a branch in `push()` for strings beginning `-j`, converting the remaining numeric portion into a negative imaginary component.
- **Observed GREEN:** 15 tests passed.

### Step 17: PUSH — invalid numeric token

- **Test prompt:** Add `test_push_invalid_token`: `push("abc")` should raise `ValueError` whose message includes `invalid token`.
- **Observed RED:** Python produced the default float-conversion error rather than the required error message.
- **Code prompt:** Wrap string parsing in `try`/`except` and raise `ValueError("Error: invalid token")` on invalid input, without breaking valid parsing.
- **Observed GREEN:** 16 tests passed.

