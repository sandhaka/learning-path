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


def test_use_assignment_in_evaluator2():
    evaluator = Evaluator()
    result = evaluator.evaluate("t = 4")
    assert evaluator.env["t"] == 4
    assert result == 4


def test_minus():
    result = Evaluator().evaluate("5 - 5")
    assert result == 0


def test_plus():
    result = Evaluator().evaluate("5 + 5")
    assert result == 10


def test_evaluator_interactively():
    result = Evaluator()
    result.evaluate("a = 5")
    result.evaluate("b = 5")
    result = result.evaluate("a + b")
    assert result == 10


def test_evaluator_interactively2():
    evaluator = Evaluator()
    evaluator.evaluate("a = 5")
    evaluator.evaluate("b = 5")
    evaluator.evaluate("r = a + b")
    result = evaluator.evaluate("(r / 5) - 1")
    assert result == 1


def test_evaluator_interactively3():
    evaluator = Evaluator()
    evaluator.evaluate("a = 5")
    evaluator.evaluate("b = 5")
    evaluator.evaluate("r = a + b")
    result = evaluator.evaluate("r / 5 - 1")
    assert result == 1


def test_evaluator_interactively4():
    evaluator = Evaluator()
    evaluator.evaluate("x = 5")
    evaluator.evaluate("y = x")
    assert evaluator.env["y"] == 5


def test_evaluator_interactively5():
    evaluator = Evaluator()
    evaluator.evaluate("y = x + a")
    evaluator.evaluate("x = 1")
    evaluator.evaluate("a = 1")
    result = evaluator.evaluate("y")
    assert result == 2
