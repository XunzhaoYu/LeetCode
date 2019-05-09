"""
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:
    Input:
               1
                \
                 3
                /
               2
    Output: 1
    Explanation: The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).

Note: There are at least two nodes in this BST.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        # 56 ms, faster than 100.00%.
        self.res = float('inf')
        self.prev = float('-inf')

        def check(node):
            if node.left:
                check(node.left)
            diff = node.val - self.prev
            if diff < self.res:
                self.res = diff
            self.prev = node.val
            if node.right:
                check(node.right)

        check(root)
        return self.res
