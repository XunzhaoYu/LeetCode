"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
    Given binary tree [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7

    return its bottom-up level order traversal as:
    [
      [15,7],
      [9,20],
      [3]
    ]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# queue, iteration, bfs.
def levelOrderBottom(root):  # 28 ms, faster than 60.73%; 12 MB, less than 5.08%
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    queue, res = collections.deque([(root, 1)]), []  # *** level
    while queue:
        current, level = queue.popleft()
        if current:
            if len(res) < level:
                res.append([])
            res[level - 1].append(current.val)
            queue.append((current.left, level + 1))
            queue.append((current.right, level + 1))
    return res[::-1]


# use list.pop(0) can get the same result as queue.popleft()  ***


# queue, iteration, bfs, non-level version
def levelOrderBottom2(root):  # 24 ms, faster than 100%; 12 MB, less than 5.08%
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        result.append([int(node.val) for node in queue])
        tempList = []
        for node in queue:
            if node.left:
                tempList.append(node.left)
            if node.right:
                tempList.append(node.right)
        queue = tempList
    return result[::-1]

