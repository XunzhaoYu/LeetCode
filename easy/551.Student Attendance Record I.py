"""
You are given a string representing an attendance record for a student. The record only contains the following three characters:
    'A' : Absent.
    'L' : Late.
    'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
    Input: "PPALLP"
    Output: True

Example 2:
    Input: "PPALLL"
    Output: False
"""


def checkRecord(s: str) -> bool:
    # 32 ms, same to the best solution from submissions (28 ms).
    return s.count('A') < 2 and not s.count('LLL')