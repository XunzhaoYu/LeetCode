"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
    Input: 3
    Output: [1,3,3,1]

Follow up:
    Could you optimize your algorithm to use only O(k) extra space?
"""


def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    res = [1] * (rowIndex + 1)
    for row in range(2, rowIndex + 1):
        column = 1
        while column < row/2:
            if row % 2 == 0:

                res[column] = res[-column] + res[-column - 1]  # 1 = -1 + -2
            else:
                res[-1 - column] = res[column] + res[column - 1]  # -2 = 0 + 1
            column += 1
        if column == int(row/2):
            res[column] = 2*res[-column]
    if rowIndex % 2 == 0:
        res[rowIndex // 2 + 1:] = res[:rowIndex // 2][::-1]
    else:
        res[:rowIndex // 2 + 1] = res[rowIndex // 2 + 1:][::-1]
    return res


for i in range(7):
    print(getRow(i))
    print(" ")
