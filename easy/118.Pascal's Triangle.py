"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
    Input: 5
    Output:
        [
             [1],
            [1,1],
           [1,2,1],
          [1,3,3,1],
         [1,4,6,4,1]
        ]
"""


def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    # 20 ms, faster than 73.52%, 11.7 MB, less than 5.26%.
    res = []
    for i in range(numRows):
        res.append([1])
        for j in range(1, i+1):
            if j == i:
                res[i].append(1)
            else:
                res[i].append(res[i-1][j-1]+res[i-1][j])
    return res


def generate2(numRows):
    # 20 ms, faster than 73.52%, 11.7 MB, less than 5.26%.
    res = []
    if numRows > 0:
        res.append([1])
    for row in range(1, numRows):
        res.append([1, 1])
        column = 1
        while column < row / 2:
            temp = res[row - 1][column - 1] + res[row - 1][column]
            res[row].insert(column, temp)
            res[row].insert(column, temp)
            column += 1
        if column == row / 2:
            temp = res[row - 1][column - 1] + res[row - 1][column]
            res[row].insert(column, temp)
    return res


def generate3(numRows):
    # 20 ms, faster than 73.52%, 11.7 MB, less than 5.26%.
    output = []
    for i in range(numRows):
        if i <= 1:
            previous = [1] * (i+1)  # idea *** previous
            output.append(previous)
        else:
            temp = [1]
            for j in range(len(previous)-1):
                temp.append(previous[j] + previous[j+1])
            previous = temp + [1]
            output.append(previous)
    return output
