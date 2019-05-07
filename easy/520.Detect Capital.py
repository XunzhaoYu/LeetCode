"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:
    1.All letters in this word are capitals, like "USA".
    2.All letters in this word are not capitals, like "leetcode".
    3.Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.

Example 1:
    Input: "USA"
    Output: True

Example 2:
    Input: "FlaG"
    Output: False

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
"""


def detectCapitalUse(word: str) -> bool:
    # 40 ms, faster than 96.30%.
    if len(word) == 1:
        return True
    if word[0].islower():
        return word.islower()
    elif word[1].islower():
        return word[1:].islower()
    else:
        return word.isupper()


def detectCapitalUse2(word: str) -> bool:
    # 40 ms, faster than 96.30%. The best solution from submissions (36 ms).
    return word.isupper() or word.islower() or word.istitle() # *** istitle()


print(detectCapitalUse("USA"))
print(detectCapitalUse("leetcode"))
print(detectCapitalUse("Google"))
print(detectCapitalUse("A"))
print(detectCapitalUse("a"))
print(detectCapitalUse("flaG"))
print(detectCapitalUse("GameOfThrone"))