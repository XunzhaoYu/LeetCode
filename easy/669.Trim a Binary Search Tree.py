"""
Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L).
You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.

Example 1:
    Input:
            1
           / \
          0   2

          L = 1
          R = 2

    Output:
            1
              \
               2

Example 2:
    Input:
            3
           / \
          0   4
           \
            2
           /
          1

          L = 1
          R = 3

    Output:
              3
             /
           2
          /
         1
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def trimBST(root: TreeNode, L: int, R: int) -> TreeNode:
    # 52 ms, faster than 97.68%. The best solution from submissions tested to be 56 ms (44 ms)
    if root:
        if root.val < L:
            return trimBST(root.right, L, R)
        elif root.val > R:
            return trimBST(root.left, L, R)
        else:
            root.left = trimBST(root.left, L, R)
            root.right = trimBST(root.right, L, R)
            return root
    return None

