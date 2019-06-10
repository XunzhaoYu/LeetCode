"""
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:

Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
Note:

letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.
"""


def nextGreatestLetter(letters: List[str], target: str) -> str:
    # 36 ms, faster than 94.16%.
    tar = ord(target)
    if ord(letters[-1]) <= tar:
        return letters[0]
    sp, ep = 0, len(letters) - 1
    while sp < ep:
        mid = (sp + ep) // 2
        order = ord(letters[mid])
        if order <= tar:
            sp = mid + 1
        else:
            ep = mid
    return letters[sp]

    # best solution is 24ms, same method, but char can be compared directly, ord() function is not necessary.