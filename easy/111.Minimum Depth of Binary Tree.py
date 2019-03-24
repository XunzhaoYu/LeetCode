"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:
    Given binary tree [3,9,20,null,null,15,7],
                3
               / \
              9  20
                /  \
               15   7
    return its minimum depth = 2.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive solution: 40 ms
def minDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root:
        if root.left and root.right:
            return min(minDepth(root.left), minDepth(root.right))+1
        else:
            return (minDepth(root.left) or minDepth(root.right)) + 1
    return 0


# Iterative solution: 32 ms faster than 96.14%, best one is 28 ms but tested to be same/worse to my result.
def minDepth2(root):
    if not root:
        return 0
    queue, res = [root], 1
    while queue:
        temp_queue = []
        for node in queue:
            if not node.left and not node.right:
                return res
            if node.left:
                temp_queue.append(node.left)
            if node.right:
                temp_queue.append(node.right)
        queue = temp_queue
        res += 1


# *** The node with one child is not a leaf, height related problems
