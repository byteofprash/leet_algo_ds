"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
"""


def isSymmetric(root):
    def get_vals_dfs(node, vals):
        if node is not None:
            get_vals_dfs(node.left, vals)
            if node.left is None and node.right is not None:
                vals.append("null")
            vals.append(node.val)
            print(node.val)
            if node.left is not None and node.right is None:
                vals.append("null")
            get_vals_dfs(node.right, vals)
        else:
            vals.append("null")
        return vals

    def get_vals_bfs(node, vals):
        visited = []
        if node:
            visited.append(node)
            print(node.val)
        current = node
        while current:
            text = ''
            if current.left:
                print(current.left.val)
                visited.append(current.left)
            if current.right:
                print(current.right.val)
                visited.append(current.right)
            for i in visited:
                text = text + str(i.val) + " "
            print(text)
            visited.pop(0)
            if not visited:
                break
            current = visited[0]

    def get_vals_bylevels(node, vals):
        parents = []
        results = []
        if node:
            parents.append(node)
            # print(node.val)
            results.append([node.val])
        while len(parents) > 0:
            new_parents = []
            for current in parents:
                if current.left:
                    # print(current.left.val)
                    new_parents.append(current.left)
                elif current.right:
                    new_parents.append(Node(None))
                if current.right:
                    # print(current.right.val)
                    new_parents.append(current.right)
                elif current.left:
                    new_parents.append(Node(None))
            results.append([parent.val for parent in new_parents])
            parents = new_parents
        return results

        # return vals

    vals = []
    results = get_vals_bylevels(root, vals)
    print(results)
    for values in results:
        r = len(values) // 2
        l = r - 1
        while r != len(values):
            if l >= 0 and r >= 0 and values[l] != values[r]:
                return False
            l-=1
            r+=1

    return True


class Node():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# n = Node(None)
n = Node(2)

n.left = Node(3)
n.left.left = Node(4)
# n.left.left.left = Node(1)
# n.left.left.right = Node(2)
n.left.right = Node(5)
n.left.right.left = Node(8)
n.left.right.left = Node(9)

n.right = Node(3)
n.right.left = Node(5)
# n.right.left.left = Node(1)
# n.right.left.right = Node(2)
n.right.right = Node(4)
n.right.right.left = Node(2)
n.right.right.left = Node(9)
n.right.right.left = Node(8)
# n = Node(1)

# n.left = Node(2)
# n.left.left = Node(3)
# # n.left.left.left = Node(1)
# # n.left.left.right = Node(2)
# n.left.right = Node(4)
# # n.left.right.left = Node(2)

# n.right = Node(2)
# n.right.left = Node(4)
# # n.right.left.left = Node(1)
# # n.right.left.right = Node(2)
# n.right.right = Node(3)
# # n.right.right.left = Node(2)


print(isSymmetric(n))
