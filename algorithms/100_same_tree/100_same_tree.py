"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""


def isSameTree(p, q):
    """

    :param p: TODO
    :param q: TODO
    :returns: TODO

    """
    def get_vals(node, vals):
        """TODO: Docstring for .

        :param node: TODO
        :returns: TODO

        """
        if node is not None:
            get_vals(node.left, vals)
            if node.left is None and node.right is not None:
                vals.append("null")
            vals.append(node.val)
            print(node.val)
            if node.left is not None and node.right is None:
                vals.append("null")
            get_vals(node.right, vals)
        
        return vals

    values = []
    values_p = get_vals(p, values)
    values = []
    values_q = get_vals(q, values)

    print(values_p, values_q)
    if values_p == values_q:
        return True
    else:
        return False


class Node():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


n = Node(1)
n.left = Node(1)
# n.right = Node(1)

m = Node(1)
# m.left = Node(1)
m.right = Node(1)

print(isSameTree(n, m))
