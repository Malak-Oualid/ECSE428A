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

_Add your prompts here (or note that this part was written without AI)._
