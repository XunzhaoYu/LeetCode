"""
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:

Input:
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
Note:

The boundaries of each input argument are 1 <= left <= right <= 10000.
"""


def selfDividingNumbers(left: int, right: int) -> List[int]:
    # 48 ms, faster than 94.30%. Same as the best solution from submissions(32 ms)
    def selfDivide(n):
        num = n
        while num:
            num, digit = divmod(num, 10)
            if not digit:
                return False
            elif n % digit:
                return False
        return True

    return [n for n in range(left, right + 1) if selfDivide(n)]
