"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example, given a 3-ary tree:

                1
            3   2   4
        5   6

We should return its max depth, which is 3.

Note:
    The depth of the tree is at most 1000.
    The total number of nodes is at most 5000.
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
def maxDepth(root: 'Node') -> int:
    # 76 ms, faster than 99.96%
    depth = 0
    if root:
        queue = [(root, 1)]
        while queue:
            node, depth = queue.pop(0)
            for child in node.children:
                queue.append((child, depth+1))
    return depth


def maxDepth2(root: 'Node') -> int:
    # 72 ms, the best solution from submissions.
    q,depth = root and [root], 0
    while q:
        q, depth = [child for node in q for child in node.children if child], depth+1 # *** for for
    return depth
