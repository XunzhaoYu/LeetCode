"""
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.

Example 1:
    Input: words = ["w","wo","wor","worl", "world"]
    Output: "world"
    Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Example 2:
    Input: words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    Output: "apple"
    Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".

Note:
    All the strings in the input will only contain lowercase letters.
    The length of words will be in the range [1, 1000].
    The length of words[i] will be in the range [1, 30].
"""


def longestWord(words):# List[str]) -> str:
    # 44 ms, faster than 98.47%.
    words.sort(key=len)  # ***
    candidate = words[0]
    existing = dict()
    for word in words:
        if len(word) == 1:
            existing[word] = 1
        if existing.get(word[:-1]):
            existing[word] = 1
            if len(candidate) < len(word) or (len(candidate) == len(word) and word < candidate):
                candidate = word
    return candidate

def longestWord2(words):# List[str]) -> str:
    # 44 ms, (36 ms) 从后往前，一个个确认
    sortedWords = sorted(words, key=len, reverse=True)
    words = set(words)
    for word in sortedWords:
        found = True
        for i in range(1, len(word)):
            if word[:i] not in words:
                found = False
                break
        if found:
            return word
    return ""

def longestWord3(words):# List[str]) -> str:
    dic = {}
    max = 0
    for s in words:
        l = len(s)
        if l not in dic:
            dic[l] = [s]
            if l > max:
                max = l
        else:
            dic[l].append(s)
    res = max
    for i in range(2, max + 1):
        if i in dic:
            temp = []
            for s in dic[i]:
                if s[:-1] in dic[i - 1]:
                    temp.append(s)
            if not temp:
                res = i - 1
                break
            else:
                dic[i] = temp
        else:
            res = i - 1
            break
    sorted_words = sorted(dic[res])
    return sorted_words[0]
