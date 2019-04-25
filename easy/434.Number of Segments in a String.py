"""
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:
    Input: "Hello, my name is John"
    Output: 5
"""


def countSegments(s: str) -> int:
    # 36 ms, faster than 76.40%. The best solution from submissions (28 ms).
    return len(s.split())


def countSegments2(s: str) -> int:
    # 36 ms, faster than 76.40%.
    res, segment = 0, 0
    for c in s:
        if c == " " and segment == 1:  # end of a segment.
            segment = 0
        elif c != " " and segment == 0:  # start of a segment.
            segment = 1
            res += 1
    return res


print(countSegments(""))
print(countSegments("        "))
print(countSegments("Hello, my name is John"))