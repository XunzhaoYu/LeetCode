"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

    root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

                  10
                 /  \
                5   -3
               / \    \
              3   2   11
             / \   \
            3  -2   1

    Return 3. The paths that sum to 8 are:

            1.  5 -> 3
            2.  5 -> 2 -> 1
            3. -3 -> 11
"""

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def pathSum(root: TreeNode, sum: int) -> int:
    """ Wrong solution. If the root.val == sum, it cannot search deeper area.
    def pathSumExtend(root: TreeNode, sub_sum: int, included: int) -> int:
        if not root:
            return 0
        if root.val == sub_sum:
            return 1 + pathSumExtend(root.left, 0, 1) + pathSumExtend(root.right, 0, 1)

        new_sum = sub_sum - root.val
        res_included = pathSumExtend(root.left, new_sum, 1) + pathSumExtend(root.right, new_sum, 1)
        if included == 1:
            return res_included
        else:
            return pathSumExtend(root.left, sub_sum, 0) + pathSumExtend(root.right, sub_sum, 0) + res_included

    if root:
        return pathSumExtend(root, sum, 0) if root.val != sum else 1 + pathSumExtend(root.left, sum, 0) + pathSumExtend(root.right, sum, 0)
    else:
        return 0
    """

    """ # Correct solution, 984 ms, faster than 26.51%. 
    self.res=0        
         # 1.不断改变root节点计算.                
#         def allroot(root,sums):            
#             if not root:return 0
#             rootSum(root,sums)
#             allroot(root.left,sums)
#             allroot(root.right,sums)
            
#         # 2.统计以某个节点为根节点的解法,从这个节点为起点顺下来.
#         def rootSum(root,sums):
#             if root :
#                 if root.val==sums: 
#                     self.res+=1 # 如果到该节点时,已经命中返回
#                 #即使命中,也要继续访问后面的节点,因为有可能还可以命中.
#                 rootSum(root.left,sums-root.val) 
#                 rootSum(root.right,sums-root.val)
                
#         allroot(root,sums)            
#         return self.res
    """

def pathSum2(root, sum):
    # 352 ms, faster than 55.52%.
    def helper(node, origin, targets):
        if not node: return 0
        hit = 0
        for t in targets:
            if t == node.val:
                hit += 1  # count if sum == target
        targets = [t - node.val for t in targets] + [origin]  # update the targets
        return hit + helper(node.left, origin, targets) + helper(node.right, origin, targets)

    return helper(root, sum, [sum])


def pathSum3(root, sum):
    # 52 ms, faster than 100%, the best solution from submissions. See the problem 303: range sum query - immutable. *** idea
    def traverse(node, cur_sum, sum_from_root, res):
        if node:
            cur_sum += node.val
            # find
            if cur_sum - sum in sum_from_root:  # 如果命中
                res += sum_from_root[cur_sum - sum]

            if cur_sum in sum_from_root:
                sum_from_root[cur_sum] += 1  # 如果当前和在历史出现过
            else:
                sum_from_root[cur_sum] = 1  # 如果没出现过, 将cur_sum添加到
            # print(node.val,'\t',cur_sum,'\t',sum_from_root,'\t',self.r)

            if node.left:
                res += traverse(node.left, cur_sum, sum_from_root, 0)  # 遍历左右分支
            if node.right:
                res += traverse(node.right, cur_sum, sum_from_root, 0)
            sum_from_root[cur_sum] -= 1
            # 这一步很关键,如果当前的分支全部被访问过,也就是之后不应该再被访问到,就应该将该分支从sum_from_root中去掉(-1)
            # 以避免其他分支计算到这条路径.
            return res

    return traverse(root, 0, {0: 1}, 0) or 0
