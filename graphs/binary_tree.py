class Tree:
    def __init__(self, left, right, item=None, parent=None):
     self.left = left
     self.right = right
     self.item = item
     self.parent = parent

    def search_tree(self, l, item):
     if l == None:
      return None
     if self.item == item:
      return l
     if item < self.item:
      return self.search_tree(self.left, item)
     else
      return self.search_tree(self.right, item)
