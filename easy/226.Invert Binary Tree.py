"""
Invert a binary tree.

Example:
    Input:

                 4
               /   \
              2     7
             / \   / \
            1   3 6   9
    Output:

                 4
               /   \
              7     2
             / \   / \
            9   6 3   1
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def invertTree(root):  # 20 ms, faster than 72.43%. But same as the best solution from submissions (16 ms)
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    queue = [root]
    while queue:
        curr = queue.pop(0)
        if curr:
            queue.append(curr.right)
            queue.append(curr.left)
            curr.left = queue[-2]
            curr.right = queue[-1]
    return root



def invertTree2(root):
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack += node.left, node.right  # ***
    return root
