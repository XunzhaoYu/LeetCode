"""
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
    Input: "abab"
    Output: True
    Explanation: It's the substring "ab" twice.

Example 2:
    Input: "aba"
    Output: False

Example 3:
    Input: "abcabcabcabc"
    Output: True
    Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""


def repeatedSubstringPattern3(s: str) -> bool:
    # 100 ms, faster than 34.22%.
    res, sl = False, len(s)
    split = 2 if sl % 2 == 0 else 3
    f_end = sl // split + 1
    f_start = s.find(s[0], 1, f_end)
    while f_start > 0:
        if sl % f_start == 0:
            sp = f_start + 1
            while sp < 2 * f_start:
                if s[sp] != s[sp - f_start]:
                    break
                else:
                    sp += 1
            if sp == 2 * f_start:
                print(f_start)
                end, res = sp + f_start, True
                while end <= sl:
                    if s[0:f_start] != s[end - f_start:end]:
                        res = False
                        break
                    end += f_start
                if res:
                    return res
        f_start = s.find(s[0], f_start + 1, f_end)
    return res


def repeatedSubstringPattern2(s: str) -> bool:
    # 44 ms, faster than 72.57%
    sl = len(s)
    if sl % 2 == 0:
        mid = sl // 2
        if s[:mid] == s[mid:]:
            return True
    prime, dp = [], sl // 2 + 1
    for num in range(3, dp, 2):
        if sl % num == 0:
            tested = False
            for p in prime:
                if num % p == 0:
                    tested = True
                    break

            if not tested:
                len_sub = sl // num
                mid = num // 2
                if s[:(mid + 1) * len_sub] == s[mid * len_sub:]:
                    return True
                else:
                    prime.append(num)
    if sl > 1 and len(set(s)) == 1:
        return True
    return False


def repeatedSubstringPattern(s: str) -> bool:
    # 32 ms, faster than 100%. The best solution from submissions.
    s1 = s + s
    return s in s1[1:-1]  # *** idea


print(repeatedSubstringPattern("aabaaba"))  # True
print(" --- 1 ---")
print(repeatedSubstringPattern("abab"))  # True
print(" --- 2 ---")
print(repeatedSubstringPattern("aba"))  # False
print(" --- 3 ---")
print(repeatedSubstringPattern("abcabcabcabc"))  # True
print(" --- 4 ---")
print(repeatedSubstringPattern("ababba"))  # False
print(" --- 5 ---")
print(repeatedSubstringPattern("aaaabaaaab"))  # True

