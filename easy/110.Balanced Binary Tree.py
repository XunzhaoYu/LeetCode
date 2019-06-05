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

# Iterative solution:
def isBalanced(root):  # 48 ms, faster than 55.75%, 13.4 MB, less than 99.13%.
    """
    :type root: TreeNode
    :rtype: bool
    """
    if root:
        level_nodes, max_level, queue = [], 0, [root]
        while queue:
            level_nodes.append([])
            temp_queue = []
            for node in queue:
                if node:
                    level_nodes[max_level].append(1)
                    temp_queue.append(node.left)
                    temp_queue.append(node.right)
                else:
                    level_nodes[max_level].append(0)
            queue = temp_queue
            max_level += 1
        # get level_nodes, [[nodes in level 1], [nodes in level 2], ... [nodes in level n]]

        lengths = [len(list) for list in level_nodes]
        current_level = max_level - 1
        while current_level > -1:
            sub_index = 0
            for index in range(lengths[current_level]):
                if level_nodes[current_level][index] != 0:
                    # if sub_index+1 < lengths[current_level+1]:
                    level_nodes[current_level][index] += max(level_nodes[current_level + 1][sub_index], level_nodes[current_level + 1][sub_index + 1])
                    sub_index += 2
                if index % 2 == 1 and abs(level_nodes[current_level][index] - level_nodes[current_level][index - 1]) > 1:
                    return False
            current_level -= 1
            # update value of level_nodes to their depth.
    return True