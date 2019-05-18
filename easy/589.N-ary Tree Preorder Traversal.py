"""
Given an n-ary tree, return the preorder traversal of its nodes' values.

For example, given a 3-ary tree:
                    1
            3       2       4
        5    6

Return its preorder traversal as: [1,3,5,6,2,4].

Note:
    Recursive solution is trivial, could you do it iteratively?
"""
# breadth first search 用 queue.  从左到右遍历，queue 右进左出； 从右到左遍历， queue 进右出
# depth first search 用 stack. 从左到右遍历，stack 左进左出； 从右到左遍历， stack 右进右出

def preorder(root: 'Node') -> List[int]:
    # 92 ms, faster than 95.45%.
    res, stack = [], [root]
    if root:
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.children:
                stack += node.children[::-1]
    return res


def preorder2(root: 'Node') -> List[int]:
    # 92 ms, the best solution from submissions (80 ms).
    stack = [root]
    l =[]
    while stack:
        tempRoot = stack.pop(0)
        if tempRoot:
            l.append(tempRoot.val)
            if tempRoot.children:
                stack = tempRoot.children + stack
    return l