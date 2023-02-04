from experiments_and_research.language_design.evaluator import Evaluator


def test_evaluator():
    result = Evaluator().evaluate("5 + 5 + 5 + 5")
    assert result == 20


def test_evaluator2():
    result = Evaluator().evaluate("5 * 5 + 5 * 5")
    assert result == 50


def test_evaluator3():
    result = Evaluator().evaluate("5 * 5 + 5")
    assert result == 30


def test_evaluator4():
    result = Evaluator().evaluate("5 * (5 + 5) * 5")
    assert result == 250


def test_use_assignment_in_evaluator():
    evaluator = Evaluator()
    result = evaluator.evaluate("a = 5")
    assert evaluator.env["a"] == 5
    assert result == 5


def test_minus():
    result = Evaluator().evaluate("5 - 5")
    assert result == 0


def test_plus():
    result = Evaluator().evaluate("5 + 5")
    assert result == 10
