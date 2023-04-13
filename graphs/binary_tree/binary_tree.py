class Tree:
    def __init__(self, item, parent=None, left=None, right=None):
        self.item = item
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"[{id(self)}]: {self.item}"

    @staticmethod
    def load(data: list):
        data_tree = Tree(data[0])
        for n in data[1:]:
            insert(n, data_tree)
        return data_tree


def search(node: Tree, item):
    if node is None:
        return None
    if node.item == item:
        return node
    if item < node.item:
        return search(node.left, item)
    else:
        return search(node.right, item)


def find_minimum(node: Tree):
    if node is None:
        return None
    minimum_node = node
    while minimum_node.left is not None:
        minimum_node = minimum_node.left
    return minimum_node


def insert(item, node: Tree = None):
    if item < node.item:
        if node.left is None:
            node.left = Tree(item, node)
        else:
            insert(item, node.left)
    elif node.right is None:
        node.right = Tree(item, node)
    else:
        insert(item, node.right)
