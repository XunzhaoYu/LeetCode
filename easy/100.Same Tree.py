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


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Recursion solution:
def isSameTree(p, q):  # 16 ms, faster than 100%; 10.6 MB, less than 47.06%
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if not p or not q:
        return not p and not q
    else:
        return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


def isSameTree2(p, q):
    if p and q:
        return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    return p is q  # *** is


# Iteration solution:  # ***
"""
    from collections import deque
    deque: a queue which can append or pop from both sides.
    
    queue = deque([(p, q), ])
    while queue:
        p, q = deq.popleft()
        if not check(p, q):  # not None
            return False
        if p:
            deq.append((p.left, q.left))
            deq.append((p.right, q.right))
"""
