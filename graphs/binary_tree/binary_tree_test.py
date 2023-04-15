from binary_tree import Tree, nodes_number, search, find_minimum, delete, traverse
from random import choice, choices, sample


def test_load():
    test_data = sample(range(1024), 32)
    tree = Tree.load(test_data)

    assert tree
    assert tree.item == test_data[0]


def test_count():
    test_data = sample(range(1024), 32)
    tree = Tree.load(test_data)

    assert nodes_number(tree) == len(test_data)


def test_find_minimum():
    test_data = sample(range(1024), 32)
    tree = Tree.load(test_data)
    minimum = find_minimum(tree)

    assert minimum
    assert minimum.item == min(test_data)


def test_search():
    test_data = sample(range(1024), 32)
    tree = Tree.load(test_data)
    n = choice(test_data)
    node = search(tree, n)

    assert node
    assert node.item == n


def test_delete():
    test_data = [2, 1, 7, 4, 8, 3, 6, 5]
    tree = Tree.load(test_data)
    delete(4, tree)

    assert search(tree, 4) is None


def test_random_delete():
    test_data = sample(range(1024), 32)
    tree = Tree.load(test_data)
    n = choice(test_data)
    delete(n, tree)

    assert nodes_number(tree) == 31
    assert search(tree, n) is None


def test_multi_random_delete():
    test_data = sample(range(1024), 32)
    tree = Tree.load(test_data)
    seq = set(choices(test_data, k=5))
    for n in seq:
        delete(n, tree)
        assert search(tree, n) is None

    assert nodes_number(tree) == 32 - len(seq)


def test_traverse():
    test_data = sample(range(1024), 32)
    tree = Tree.load(test_data)
    traverse(tree, lambda i: print(i))

    assert tree
