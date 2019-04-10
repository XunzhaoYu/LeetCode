"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

    Input:

                   1
                 /   \
                2     3
                 \
                  5

    Output: ["1->2->5", "1->3"]

    Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def binaryTreePaths(self, root: TreeNode) -> List[str]:  # 40 ms, faster than 97.54%.
    def searchPaths(root: TreeNode, prefix: str) -> List[str]:
        prefix += str(root.val) + "->"
        if root.left:
            if root.right:
                return searchPaths(root.left, prefix) + searchPaths(root.right, prefix)
            else:
                return searchPaths(root.left, prefix)
        else:
            if root.right:
                return searchPaths(root.right, prefix)
            else:
                return [prefix[:-2]]

    return searchPaths(root, "") if root else []


def binaryTreePaths2(self, root: TreeNode) -> List[str]:  # 40 ms, faster than 97.54%. Best solution from submissions (36 ms)
    self.ans = []
    if not root:
        return self.ans
    self.dfs(root, [])
    return self.ans

def dfs(self, root, path):
    path.append(str(root.val))
    if root.left == None and root.right == None:
        self.ans.append('->'.join(path))   # *** idea: self.ans 直接加,不用返回。 "str".join(),衔接字符串
    if root.left:
        self.dfs(root.left, path)
    if root.right:
        self.dfs(root.right, path)
    path.pop()