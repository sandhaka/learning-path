import numpy as np
from binary_tree import Tree, nodes_number, search, find_minimum
from random import choice


def test_load():
    test_data = list(np.random.randint(1024, size=32))
    tree = Tree.load(test_data)

    assert tree
    assert tree.item == test_data[0]


def test_count():
    test_data = list(np.random.randint(1024, size=32))
    tree = Tree.load(test_data)

    assert nodes_number(tree) == len(test_data)


def test_find_minimum():
    test_data = list(np.random.randint(1024, size=32))
    tree = Tree.load(test_data)
    minimum = find_minimum(tree)

    assert minimum
    assert minimum.item == min(test_data)


def test_search():
    test_data = list(np.random.randint(1024, size=32))
    tree = Tree.load(test_data)
    n = choice(test_data)
    node = search(tree, n)

    assert node
    assert node.item == n
