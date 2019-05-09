"""
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original
key plus sum of all keys greater than the original key in BST.

Example:
    Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

    Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
"""


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def convertBST(root: TreeNode) -> TreeNode:
        # 68 ms, faster than 100.00%. Best solution from submission tested to be 72 ms.
        def addSum(node, sum_parent):
            if node.right:
                sum_parent = addSum(node.right, sum_parent)
            node.val += sum_parent
            if node.left:
                return addSum(node.left, node.val)
            return node.val

        if root:
            addSum(root, 0)
        return root