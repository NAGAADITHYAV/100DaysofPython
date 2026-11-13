class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BST:
    def __init__(self, root = None):
        self.root = root

    def height(self):
        return self._height(self.root)
    
    def _height(self, node):
        if not node:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))