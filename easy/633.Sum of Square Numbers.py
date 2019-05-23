"""
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
    Input: 5
    Output: True
    Explanation: 1 * 1 + 2 * 2 = 5

Example 2:
    Input: 3
    Output: False
"""


def judgeSquareSum(c):# int) -> bool:
    # 112 ms, faster than 94.92%.
    start, end = 0, int(math.sqrt(c))
    s = end*end
    while start <= end:
        if s > c:
            s -= (end+end-1)
            end -= 1
        elif s < c:
            s += (start+start+1)
            start += 1
        else:
            return True
    return False


def judgeSquareSum2(c):# int) -> bool:
    # 28 ms, the best solution from submissions.
    for i in itertools.chain([2], itertools.count(3, 2)):
        count = 0
        if c % 4 == 3:
            return False
        elif c <= i * i:
            return True
            break
        while c % i == 0:
            c //= i
            count += 1
        if (i % 4 == 3 and count % 2 == 1):
            return False


