"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
    Given tree s:

         3
        / \
       4   5
      / \
     1   2
    Given tree t:
       4
      / \
     1   2
    Return true, because t has the same structure and node values with a subtree of s.

Example 2:
    Given tree s:

         3
        / \
       4   5
      / \
     1   2
        /
       0
    Given tree t:
       4
      / \
     1   2
    Return false.
"""


def isSubtree(s: TreeNode, t: TreeNode) -> bool:
    # 64 ms, faster than 100.00%.
    def isSubtree2(s, t, c):
        if not (t or s):
            return True
        if not (t and s):
            return False
        if s.val == t.val:
            return isSubtree2(s.left, t.left, True) and isSubtree2(s.right, t.right, True) or isSubtree2(s.left, t, False) or isSubtree2(s.right, t, False)
        elif c == True:
            return False
        else:
            return isSubtree2(s.left, t, False) or isSubtree2(s.right, t, False)

    return isSubtree2(s, t, False)