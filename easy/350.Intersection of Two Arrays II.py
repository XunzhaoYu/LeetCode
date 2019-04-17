from collections import Counter
"""
Given two arrays, write a function to compute their intersection.

Example 1:
    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2,2]

Example 2:
    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [4,9]

Note:
    Each element in the result should appear as many times as it shows in both arrays.
    The result can be in any order.

Follow up:
    What if the given array is already sorted? How would you optimize your algorithm?
    What if nums1's size is small compared to nums2's size? Which algorithm is better?
    What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""


def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    # 48 ms, faster than 39.39%. Delete intersection iteratively.
    intersection, res = list(set(nums1) & set(nums2)), []
    while intersection:
        res += intersection
        for n in intersection:
            nums1.remove(n)
            nums2.remove(n)
        intersection = list(set(nums1) & set(nums2))
    return res


def intersect2(nums1: list[int], nums2: list[int]) -> list[int]:
    # 44 ms, faster than 60.89%. Two pointers in sorted arrays.
    nums1.sort()
    nums2.sort()
    p1, p2, res = 0, 0, []
    while p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] == nums2[p2]:
            res.append(nums1[p1])
            p1 += 1
            p2 += 1
        elif nums1[p1] > nums2[p2]:
            p2 += 1
        elif nums1[p1] < nums2[p2]:
            p1 += 1
    return res


def intersect3(nums1: list[int], nums2: list[int]) -> list[int]:
    # 40 ms, faster than 89.23%. Best solution form submissions (32 ms). Use dictionary to count digits.
    d = {}
    result = []
    for i in nums1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for j in nums2:
        if (j in d) and (0 != d[j]):
            result.append(j)
            d[j] -= 1
    return result


def intersect4(nums1: list[int], nums2: list[int]) -> list[int]:
    # 40 ms, faster than 89.23%. Shortest solution from submissions.
    a, b = map(Counter, (nums1, nums2))  # *** map review.
    return list((a & b).elements())