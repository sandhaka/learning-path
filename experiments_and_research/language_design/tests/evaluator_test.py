import pytest

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


def test_modulo():
    result = Evaluator().evaluate("5 % 2")
    assert result == 1


def test_modulo2():
    result = Evaluator().evaluate("7 % 4")
    assert result == 3


def test_basic_arithmetic():
    evaluator = Evaluator()
    assert evaluator.evaluate("1 + 1") == 2
    assert evaluator.evaluate("2 - 1") == 1
    assert evaluator.evaluate("2 * 3") == 6
    assert evaluator.evaluate("8 / 4") == 2
    assert evaluator.evaluate("7 % 4") == 3


def test_evaluator_interactively():
    evaluator = Evaluator()
    evaluator.evaluate("a = 5")
    evaluator.evaluate("b = 5")
    result = evaluator.evaluate("a + b")
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
    evaluator.evaluate("x = 1")
    evaluator.evaluate("a = 1")
    evaluator.evaluate("y = x + a")
    result = evaluator.evaluate("y")
    assert result == 2


def test_evaluator_incorrect_seq():
    evaluator = Evaluator()
    try:
        evaluator.evaluate("y")
    except RuntimeError as e:
        assert str(e) == "y is not defined"


def test_evaluator_incorrect_seq2():
    evaluator = Evaluator()
    try:
        evaluator.evaluate("x = 1")
        evaluator.evaluate("y = x + a")
        evaluator.evaluate("a = 1")
    except RuntimeError as e:
        assert str(e) == "a is not defined"


def test_evaluator_incorrect_seq3():
    evaluator = Evaluator()
    assert evaluator.evaluate("x = 1") == 1
    assert evaluator.evaluate("x") == 1
    assert evaluator.evaluate("x + 3") == 4
    try:
        evaluator.evaluate("y")
        assert False
    except RuntimeError as e:
        assert str(e) == "y is not defined"


def test_wrong_input():
    evaluator = Evaluator()
    with pytest.raises(Exception):
        evaluator.evaluate("1.4.5")


def test_wrong_input2():
    evaluator = Evaluator()
    with pytest.raises(Exception):
        evaluator.evaluate("1 5")
