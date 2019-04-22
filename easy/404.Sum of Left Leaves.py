"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""


def sumOfLeftLeaves(root: TreeNode) -> int:
    # iterative solution: 40 ms, faster than 82.50%
    res = 0
    if root:
        queue = [(root, 0)]
        while queue:
            node, loc = queue.pop(0)
            if node.left or node.right:
                if node.left:
                    queue.append((node.left, 1))
                if node.right:
                    queue.append((node.right, 2))
            elif loc == 1:
                    res += node.val
    return res


def sumOfLeftLeaves2(root: TreeNode) -> int:
    # recursive solution: 40 ms, faster than 82.50%
    def sumOfLeft(root: TreeNode, loc: int):
        if root:
            if root.left or root.right:
                return sumOfLeft(root.left, 1) + sumOfLeft(root.right, 2)
            elif loc == 1:
                return root.val
        return 0

    return 0 if not root else sumOfLeft(root.left, 1) + sumOfLeft(root.right, 2)


def sumOfLeftLeaves3(root: TreeNode) -> int:
    # 40 ms, faster than 82.50%, best solution from submissions (32 ms).
    if not root:
        return 0

    total = 0

    if root.left:
        if not root.left.left and not root.left.right:
            total += root.left.val
        else:
            total += self.sumOfLeftLeaves(root.left)

    if root.right:
        total += self.sumOfLeftLeaves(root.right)

    return total


