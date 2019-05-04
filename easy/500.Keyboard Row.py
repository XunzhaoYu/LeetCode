"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

Example:
    Input: ["Hello", "Alaska", "Dad", "Peace"]
    Output: ["Alaska", "Dad"]

Note:
    You may use one character in the keyboard more than once.
    You may assume the input string will only contain letters of alphabet.
"""


def findWords(words: List[str]) -> List[str]:
    # 36 ms, faster than 79.38%. Same to the best solution from submissions (28 ms).
    row1 = set('qwertyuiop')
    row2 = set('asdfghjkl')
    row3 = set('zxcvbnm')
    res = []
    for w in words:
        temp = set(w.lower())
        if not temp.difference(row1) or not temp.difference(row2) or not temp.difference(row3):
            res.append(w)
    return res


print(findWords(["Hello", "Alaska", "Dad", "Peace"]))
