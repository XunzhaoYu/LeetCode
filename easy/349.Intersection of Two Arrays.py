"""
Given two arrays, write a function to compute their intersection.

Example 1:
    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2]

Example 2:
    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [9,4]

Note:
    Each element in the result must be unique.
    The result can be in any order.
"""


def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    # 40 ms, faster than 83.74%.
    s1, s2 = set(nums1), set(nums2)
    return list(s1.intersection(s2))


def intersection2(nums1: list[int], nums2: list[int]) -> list[int]:
    # 40 ms, faster than 83.74%. Best solution from submissions (32 ms)
    return list(set(nums1) & set(nums2))  # *** & in set operations.