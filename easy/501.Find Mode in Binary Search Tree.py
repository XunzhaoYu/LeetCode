"""
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.


For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2


return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def findMode(root: TreeNode) -> List[int]:
    # 72 ms, faster than 41.02%.
    dic, queue, mode_count = {}, [root], 1
    while queue:
        node = queue.pop(0)
        if node:
            if node.val in dic:
                dic[node.val] += 1
                if dic[node.val] > mode_count:
                    mode_count = dic[node.val]
            else:
                dic[node.val] = 1
            queue.append(node.left)
            queue.append(node.right)
    return [key for key in dic if dic[key] == mode_count]
