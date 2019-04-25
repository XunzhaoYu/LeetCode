"""
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example, given a 3-ary tree:
            1
    3       2       4
  5   6

We should return its level order traversal:

[
     [1],
     [3,2,4],
     [5,6]
]
"""


def levelOrder(root: 'Node') -> list[list[int]]:
    # 100 ms, faster than 76.43%.
    res, queue = [], [root]
    if root:
        while queue:
            res.append([n.val for n in queue])
            next_queue = []
            for node in queue:
                for child in node.children:
                    next_queue.append(child)
            queue = next_queue
    return res


def levelOrder2(root: 'Node') -> list[list[int]]:
    # 100 ms, faster than 76.43%, the best solution from submissions. (88 ms)
    ans = []
    base = [root]
    while base:
        nb = []
        cur = []
        for i in base:
            if i:
                cur.append(i.val)
                nb += i.children  # *** list + list: [1, 2] + [3, 4] = [1, 2, 3, 4]
        if cur:
            ans.append(cur)
        base = nb
    return ans

