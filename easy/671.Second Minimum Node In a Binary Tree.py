"""
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node.
If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:
    Input:
            2
           / \
          2   5
             / \
            5   7

    Output: 5
    Explanation: The smallest value is 2, the second smallest value is 5.

Example 2:
    Input:
            2
           / \
          2   2

    Output: -1
    Explanation: The smallest value is 2, but there isn't any second smallest value.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(root: TreeNode) -> int:
        # 32 ms, faster than 95.01%.
        def search(root):
            if root.left:
                search(root.left)
            if root.val < self.res:
                if root.val < self.min:
                    self.res = self.min
                    self.min = root.val
                elif root.val > self.min:
                    self.res = root.val
            if root.right:
                search(root.right)

        self.min = root.val
        self.res = float('inf')
        search(root)
        return self.res if self.res != float('inf') else -1


    def findSecondMinimumValue2(root: TreeNode) -> int:
        # Best solution from submissions (20 ms), tested to be 32 ms.
        def f(node, s):
            if not node:
                return
            s.add(node.val)
            f(node.left, s)
            f(node.right, s)
        s = set()
        f(root, s)
        if len(s) < 2:
            return -1
        s.remove(min(s))
        return min(s)