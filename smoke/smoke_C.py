from src.calc import add


def test_add_must_also_return_a_string():
    # Contradicts the seed test test_add (add(2,3) == 5). Unsatisfiable by design.
    assert add(2, 3) == "23"
