"""
Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:
    Input: [1,2,3]
    Output: 3
    Explanation: Only three moves are needed (remember each move increments two elements):
            [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
"""


def minMoves(nums: List[int]) -> int:
    # 52 ms, faster than 98.03%. Same to the best solution from submissions (44 ms).
    return sum(nums) - min(nums) * len(nums)