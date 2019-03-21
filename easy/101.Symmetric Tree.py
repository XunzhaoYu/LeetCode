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

Note:
    Bonus points if you could solve it both recursively and iteratively.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Recursion solution:
def isSymmetric(root):  # 24 ms, faster than 87.21%; 12 MB, less than 5.08%
    """
    :type root: TreeNode
    :rtype: bool
    """

    def isSymmetricSubTree(left, right):
        if left and right:
            return left.val == right.val and isSymmetricSubTree(left.left, right.right) and isSymmetricSubTree(left.right, right.left)
        return left is right

    return not root or isSymmetricSubTree(root.left, root.right)


# Iteration solution:
from collections import deque
def isSymmetric(root):  # 24 ms, faster than 87.21%; 12 MB, less than 5.08%
    if not root:
        return True
    else:
        queue = deque([(root.left, root.right), ])  # normal queue is also working, but it is depth-first search.
        while queue:
            p, q = queue.popleft()
            if p and q:
                if p.val != q.val:
                    return False
                else:
                    queue.append((p.left, q.right))
                    queue.append((p.right, q.left))
            elif p is not q:
                return False
        return True
