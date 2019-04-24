"""
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
    Input: [3, 2, 1]
    Output: 1
    Explanation: The third maximum is 1.

 Example 2:
    Input: [1, 2]
    Output: 2
    Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

 Example 3:
    Input: [2, 2, 3, 1]
    Output: 1
    Explanation: Note that the third maximum here means the third maximum distinct number.
    Both numbers with value 2 are both considered as second maximum.
"""


def thirdMax(nums: List[int]) -> int:
    # 40 ms, faster than 77.91%. The best solution from submissions is same to this. (32 ms)
    num_list = list(set(nums))
    length = len(num_list)
    if length < 3:
        return max(num_list)
    else:
        max_list = num_list[:3]
        min_max = min(max_list)
        for n in num_list[3:]:
            if n > min_max:
                max_list.remove(min_max)
                max_list.append(n)
                min_max = min(max_list)
        return min_max

