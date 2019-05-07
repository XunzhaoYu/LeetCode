"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

Example 1:
    Input: 2
    Output: 1
    Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
    Input: 3
    Output: 2
    Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
    Input: 4
    Output: 3
    Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Note:
    0 ≤ N ≤ 30.
"""


def fib(N: int) -> int:
    # 36 ms, faster than 84.04%
    buff = [0, 1] + [-1] * 29
    for i in range(2, N + 1):
        buff[i] = buff[i - 2] + buff[i - 1]
    return buff[N]

    
def fib2(N: int) -> int:
    # 36 ms, faster than 84.04%, the best solution from submissions (28 ms).
    f0, f1 = 0, 1
    if N == 0: return f0
    if N == 1: return f1
    i = 2
    fn0, fn1, t = f0, f1, 0
    while(i <= N):
        t = fn1
        fn1 = fn1 + fn0
        fn0 = t
        i = i + 1
    return fn1
