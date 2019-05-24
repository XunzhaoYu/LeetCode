"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
    Input:
                5
               / \
              3   6
             / \   \
            2   4   7
    Target = 9
    Output: True

Example 2:
    Input:
                5
               / \
              3   6
             / \   \
            2   4   7
    Target = 28
    Output: False
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(root: TreeNode, k: int) -> bool:
        # 68 ms, faster than 99.95%. The best solution from submissions is 64 ms, which used the order in BST.
        dic = {}
        queue = [root]
        if root:
            while queue:
                node = queue.pop(0)
                if node.val in dic:
                    return True
                else:
                    dic[k-node.val] = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return False