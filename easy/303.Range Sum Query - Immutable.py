"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
    Given nums = [-2, 0, 3, -5, 2, -1]

    sumRange(0, 2) -> 1
    sumRange(2, 5) -> -1
    sumRange(0, 5) -> -3

Note:
    You may assume that the array does not change.
    There are many calls to sumRange function.
"""


class NumArray:
    # 52 ms, faster than 91.58%, same to the best solution from submissions(44 ms)
    def __init__(self, nums: List[int]):
        s, self.s_list = 0, [0]
        for n in nums:
            s += n
            self.s_list.append(s)

    def sumRange(self, i: int, j: int) -> int:
        return self.s_list[j+1] - self.s_list[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)