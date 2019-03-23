"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:
    Given the following tree [3,9,20,null,null,15,7]:
                3
               / \
              9  20
                /  \
               15   7
    Return true.

Example 2:
    Given the following tree [1,2,2,3,3,null,null,4,4]:
                   1
                  / \
                 2   2
                / \
               3   3
              / \
             4   4
    Return false.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def isBalanced(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if root:
        queue, heights = collections.deque([(root, 1)]), []
        while queue:
            node, height = queue.popleft()
            if node:
                queue.append((node.left, height+1))
                queue.append((node.right, height+1))
            else:
                heights.append(height-1)
        print(heights)
        if heights[-1] - heights[0] > 1:
            return False
    return True