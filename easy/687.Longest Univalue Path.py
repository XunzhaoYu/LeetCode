"""
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.

Example 1:
    Input:

                  5
                 / \
                4   5
               / \   \
              1   1   5
    Output: 2

Example 2:
    Input:

                  1
                 / \
                4   5
               / \   \
              4   4   5
    Output: 2

Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
"""


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:
    def longestUnivaluePath(self, root):# TreeNode) -> int:
        # 332 ms, faster than 100%.
        self.res = 1

        def longestPath(root):
            value, length = root.val, 1
            if root.left:
                v1, l1 = longestPath(root.left)
                if root.val == v1:
                    length += l1
            if root.right:
                v2, l2 = longestPath(root.right)
                if root.val == v2:
                    if length > 1:
                        length = max(length, 1 + l2)
                        self.res = max(self.res, l1 + l2 + 1)
                    else:
                        length += l2
            if length > self.res:
                self.res = length
            return value, length

        if root:
            longestPath(root)
        return self.res - 1
