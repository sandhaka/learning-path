class Tree:
    def __init__(self, item, left=None, right=None):
        self.item = item
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


def nodes_number(node: Tree):
    return 0 if node is None else 1 + nodes_number(node.left) + nodes_number(node.right)


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


def delete(item, node: Tree):
    if item is None or node is None:
        return None
    if item > node.item:
        node.right = delete(item, node.right)
    elif item < node.item:
        node.left = delete(item, node.left)
    else:
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        current = node.right
        while current.left is not None:
            current = current.left
        node.item = current.item
        node.right = delete(node.item, node.right)
    return node


def traverse(node: Tree, process_item):
    if node is not None:
        traverse(node.left, process_item)
        process_item(node.item)
        traverse(node.right, process_item)
