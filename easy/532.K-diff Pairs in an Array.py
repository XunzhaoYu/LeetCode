from collections import Counter
"""
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:
    Input: [3, 1, 4, 1, 5], k = 2
    Output: 2
    Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
    Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:
    Input:[1, 2, 3, 4, 5], k = 1
    Output: 4
    Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:
    Input: [1, 3, 1, 5, 4], k = 0
    Output: 1
    Explanation: There is one 0-diff pair in the array, (1, 1).

Note:
    The pairs (i, j) and (j, i) count as the same pair.
    The length of the array won't exceed 10,000.
    All the integers in the given input belong to the range: [-1e7, 1e7].
"""


def findPairs(nums: List[int], k: int) -> int:
    # 56 ms, faster than 59.41%.
    uni_nums = sorted(list(set(nums)))
    if k:
        start, end, nl, res = 0, 1, len(uni_nums), 0
        while end < nl:
            diff = uni_nums[end] - uni_nums[start]
            if diff > k and end - start > 1:
                start += 1
                continue
            elif diff == k:
                res += 1
                start += 1
            end += 1
        return res
    else:
        for n in uni_nums:
            nums.remove(n)
        return len(set(nums))


def findPairs2(nums: List[int], k: int) -> int:
    # 32 ms, the best solution from submissions.
    return len(set(nums)&{n+k for n in nums}) if k>0 else sum(v>1 for v in Counter(nums).values()) if k==0 else 0  # *** set & {}, if if else


print(findPairs([-1,0,0,1,0,0,-1], 1))  # 2
print(findPairs([-1,0,0,1,0,0,-1], 0))  # 2
