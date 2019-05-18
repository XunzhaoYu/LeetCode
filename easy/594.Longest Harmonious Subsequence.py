from collections import Counter
"""
We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
    Input: [1,3,2,2,5,2,3,7]
    Output: 5
    Explanation: The longest harmonious subsequence is [3,2,2,2,3].

Note: The length of the input array will not exceed 20,000.
"""


def findLHS(nums: List[int]) -> int:
    # 92 ms, faster than 78.40%.
    counter = Counter(nums)
    elements = sorted([e for e in counter])
    res = 0
    for i in range(len(elements) - 1):
        if elements[i + 1] - elements[i] == 1:
            res = max(counter[elements[i + 1]] + counter[elements[i]], res)
    return res


def findLHS2(nums: List[int]) -> int:
    # 72 ms, faster than 99.71%. The best solution from submissions (68 ms).
    c = collections.Counter(nums)
    max_val = 0
    for x in c:
        if x + 1 in c:  # ***
            max_val = max(max_val, c[x] + c[x+1])
    return max_val