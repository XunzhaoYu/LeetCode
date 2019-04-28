"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:
    Input: [4,3,2,7,8,2,3,1]
    Output: [5,6]
"""


def findDisappearedNumbers(nums: list[int]) -> list[int]:
    # 140 ms, faster than 92.57%.
    return list(set(range(1, len(nums) + 1)).difference(set(nums)))


def findDisappearedNumbers2(nums: list[int]) -> list[int]:
    # 136 ms, faster than 96.81%, the best solution from submissions.(120 ms)
    seen = [0] * (len(nums) + 1)
    for i in nums:
        seen[i] = 1
    return [i for i in range(1,len(nums)+1) if not seen[i]]


print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
