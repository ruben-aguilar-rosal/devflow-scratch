# tickets

Hand-authored dev-flow step fixtures for agentic-os M4 (Gates A/B/C/D).

## A-1 — add a `multiply(a, b)` function to src/calc.py

**Brief.** The seed module `src/calc.py` has `add`. Add a `multiply(a, b)` function beside it that
returns the product of two integers. Small, self-contained — designed to pass on the first attempt.

**Acceptance criteria.**
- `src/calc.py` exports a `multiply(a, b)` function.
- `multiply(a, b)` returns `a * b` for integer inputs.
- The existing `add` function and its test are untouched and still pass.

**Smoke tests (independent intent oracle — the maker did NOT write these).**
Create `tests/test_smoke_A.py` is NOT required of the maker; the checker supplies and runs this
independent smoke test against the maker's branch:

```python
# smoke_A.py — the independent intent oracle for A-1 (run by the checker, not the maker)
from src.calc import multiply

def test_multiply_basic():
    assert multiply(3, 4) == 12

def test_multiply_zero():
    assert multiply(0, 9) == 0

def test_multiply_negative():
    assert multiply(-2, 5) == -10
```

Run with: `python -m pytest smoke_A.py -q` from the repo root (the checker places `smoke_A.py` at the
root and runs it against the branch).

**Validation / quality plan.** `multiply` is a pure function; the maker writes its own unit tests
too. No new dependencies. Passing the independent smoke test above certifies the step did what was
asked.

## B-1 — add a `divide(a, b)` function to src/calc.py

**Brief.** Add a `divide(a, b)` function beside `add` in `src/calc.py`. Implement **exactly** the
acceptance criteria below and nothing more — do not infer or add unstated behavior; keep it minimal.
An independent checker will verify your work against smoke tests you do not control and cannot see
until after you push.

**Acceptance criteria.**
- `src/calc.py` exports a `divide(a, b)` function.
- `divide(a, b)` returns the result of dividing `a` by `b`.
- The existing `add` function and its test are untouched and still pass.

**Smoke tests (independent intent oracle — authored WITH the ticket, NOT by the maker).** The checker
runs `smoke/smoke_B.py` (already in the repo, which you must not read or modify) against your branch.
It certifies intent. Passing it is the bar.

**Validation / quality plan.** This ticket is engineered to exercise the maker→checker→**Reflexion**
loop (Gate B). The acceptance criteria are intentionally minimal and **deliberately hide the exact
return contract**: the smoke test requires `divide` to return an **integer, banker's-rounded to zero
decimal places** (`divide(7, 2) == 4`, `divide(5, 2) == 2` by round-half-to-even), NOT the ordinary
float `a / b`. A sensible from-spec first attempt returns `a / b` (a float) and **fails the smoke
test**; the checker's line-referenced REJECT names the rounding contract; the driver injects that
reason into a fresh maker, whose second attempt returns `round(a / b)` (Python's `round` is
banker's-rounding) and passes. Proves the loop iterates on feedback the maker could not have guessed
from the spec — not that the code is hard.

## C-1 — make `add` return both a sum AND satisfy a contradictory smoke test

**Brief.** This step is **deliberately unsatisfiable** — it exists to prove bounded escalation
(Gate C). The acceptance criteria and the independent smoke test contradict each other, so no maker
can produce code that passes: the loop must exhaust its cap of 3 maker→checker rounds and escalate
to a labeled PR, never merging.

**Acceptance criteria.**
- `src/calc.py`'s `add(a, b)` must continue to return the integer sum `a + b` (the seed test
  `tests/test_calc.py::test_add` asserts `add(2, 3) == 5` and must keep passing).

**Smoke tests (independent intent oracle — the maker did NOT write these).**

```python
# smoke_C.py — a CONTRADICTORY intent oracle for C-1 (run by the checker, not the maker)
from src.calc import add

def test_add_must_also_return_a_string():
    # Contradicts the seed test test_add (which requires add(2,3) == 5, an int).
    # No single implementation of add can satisfy both this and test_add → unsatisfiable.
    assert add(2, 3) == "23"
```

Run with: `python -m pytest smoke_C.py tests/test_calc.py -q` from the repo root — the checker runs
**both** the contradictory smoke test AND the seed test, so any implementation fails one of them.

**Validation / quality plan.** There is no valid implementation: `add(2, 3)` cannot be both `5`
(seed test) and `"23"` (smoke test). Every attempt is correctly REJECTed; after cap-3 the driver
escalates — PR left open + labeled `needs-human`, `tickets.md` marked, reject-trail posted as a PR
comment, `result.status="escalated"`. (The maker must NOT edit either test to "resolve" the
contradiction — the checker's anti-cheat item catches a weakened/edited oracle and REJECTs.)

## D-1 — add a `square(n)` one-liner (trivial ticket for the L2 write-path harness)

**Brief.** The Gate-D L2 write-path safety harness needs a coherent-but-trivial ticket so the maker
has something real to build while the harness proves the positive write path (branch push + PR open
+ label, under bypassPermissions, never merged) and the negative legs. Add a `square(n)` function to
`src/calc.py` returning `n * n`.

**Acceptance criteria.**
- `src/calc.py` exports `square(n)` returning `n * n`.
- Existing functions untouched.

**Smoke tests (independent intent oracle — the maker did NOT write these).**

```python
# smoke_D.py — the independent intent oracle for D-1 (run by the checker, not the maker)
from src.calc import square

def test_square():
    assert square(5) == 25
    assert square(0) == 0
    assert square(-3) == 9
```

Run with: `python -m pytest smoke_D.py -q` from the repo root.

**Validation / quality plan.** Trivial pure function; the point of D-1 is exercising the *write path*
(the maker pushes a branch + opens a PR under the scoped token + deny-floor + branch protection), not
the difficulty of the code. The four negative legs (§8) are proven independently by the harness.

