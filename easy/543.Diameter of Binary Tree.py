"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
    Given a binary tree
              1
             / \
            2   3
           / \
          4   5
    Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 44 ms, faster than 99.97%.
        self.res = 0

        def pathOfChildren(node):
            left = node.left and pathOfChildren(node.left) or 0
            right = node.right and pathOfChildren(node.right) or 0
            self.res = max(self.res, left + right)
            return max(left, right) + 1

        if root:
            pathOfChildren(root)
        return self.res

    def diameterOfBinaryTree2(self, root: TreeNode) -> int:
        # 36 ms, faster than 100.00%. Better than the best solution from submissions (40 ms).
        self.res = 0

        def pathOfChildren(node):
            left, right = 0, 0
            if node.left:
                left = max(pathOfChildren(node.left)) + 1
            if node.right:
                right = max(pathOfChildren(node.right)) + 1
            path_length = left + right
            if path_length > self.res:
                self.res = path_length
            return left, right

        if root:
            pathOfChildren(root)
        return self.res