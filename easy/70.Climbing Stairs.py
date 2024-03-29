"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:
    Input: 2
    Output: 2
    Explanation: There are two ways to climb to the top.
        1. 1 step + 1 step
        2. 2 steps

Example 2:
    Input: 3
    Output: 3
    Explanation: There are three ways to climb to the top.
        1. 1 step + 1 step + 1 step
        2. 1 step + 2 steps
        3. 2 steps + 1 step
"""


def climbStairs(n):  # 16 ms, faster than 100%; 10.7 MB, less than 81.64%
    """
    :type n: int
    :rtype: int
    """
    if n < 3:
        return n
    memory = [1, 2]
    for index in range(2, n):
        memory.append(memory[index-1] + memory[index-2])
    return memory[-1]


test_input = 2
print(climbStairs(test_input))  # 2
test_input = 3
print(climbStairs(test_input))  # 3
