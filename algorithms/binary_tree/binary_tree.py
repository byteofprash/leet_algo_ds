"""
Binary tree implementation
"""


class Node(object):

    """Node for a binary tree"""

    def __init__(self, val):
        """Creates a node for the binary tree

        :param val: TODO

        """
        self.val = val
        self.left = None
        self.right = None


class BinaryTree(object):

    """Binary tree implementation"""

    def __init__(self):
        """Creates a binary tree with the given values """
        self.root = None

    def add(self, val):
        """Adds the value to the binary tree

        :param val: TODO
        :returns: TODO

        """
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.val:
            if node.left is not None:
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right is not None:
                self._add(val, node.right)
            else:
                node.right = Node(val)

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)
            print(str(node.val) + " ")
            self._print_tree(node.right)

    def add_values(self, values):
        """Adds an array of items

        :param values: TODO
        :returns: TODO

        """
        for val in values:
            self.add(val)
