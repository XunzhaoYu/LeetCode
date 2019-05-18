"""
Given an n-ary tree, return the postorder traversal of its nodes' values.

For example, given a 3-ary tree:
                    1
            3       2       4
        5    6

Return its postorder traversal as: [5,6,3,2,4,1].

Note:
    Recursive solution is trivial, could you do it iteratively?
"""


def postorder(root: 'Node') -> List[int]:
    # 从左至右遍历，最后访问父节点
    # 100 ms, faster than 69.43%.
    res, stack = [], [root]
    if root:
        while stack:
            node = stack.pop(0)
            if node.children:
                stack = node.children + [Node(node.val, None)] + stack
            else:
                res.append(node.val)
    return res


def postorder2(root: 'Node') -> List[int]:
    # 从右至左遍历， 先访问父节点
    # 88 ms, faster than 99.37%. The best solution from submissions (80 ms)
    res, stack = [], [root]
    if root:
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.children:
                stack += node.children
    return res[::-1]