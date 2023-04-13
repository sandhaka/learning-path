import numpy as np
from binary_tree import Tree, search, find_minimum
from random import choice

test_data = list(np.random.randint(1024, size=32))
tree = Tree.load(test_data)


minimum = find_minimum(tree)
print(f"Minimum: {minimum} ({min(test_data)})")

n = choice(test_data)

node = search(tree, n)
print(f"Search for node {n}. Found: {node}")
