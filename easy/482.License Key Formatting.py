"""
You are given a license key represented as a string S which consists only alphanumeric character and dashes. The string is separated into N+1 groups by N dashes.

Given a number K, we would want to reformat the strings such that each group contains exactly K characters, except for the first group which could be shorter than K, but still must contain at least one character. Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.

Given a non-empty string S and a number K, format the string according to the rules described above.

Example 1:
    Input: S = "5F3Z-2e-9-w", K = 4
    Output: "5F3Z-2E9W"
    Explanation: The string S has been split into two parts, each part has 4 characters.
    Note that the two extra dashes are not needed and can be removed.

Example 2:
    Input: S = "2-5g-3-J", K = 2
    Output: "2-5G-3J"
    Explanation: The string S has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.

Note:
    The length of string S will not exceed 12,000, and K is a positive integer.
    String S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9) and dashes(-).
    String S is non-empty.
"""


def licenseKeyFormatting(S: str, K: int) -> str:
    # 84 ms, faster than 37.27%.
    S, res = S.replace("-", "").upper(), ""
    sections, first_len = divmod(len(S), K)
    for i in range(first_len, len(S), K):
        res = res + "-" + S[i:i + K]
    return res[1:] if first_len == 0 else S[:first_len] + res


def licenseKeyFormatting2(S: str, K: int) -> str:
    # 40 ms, faster than 99.57%. The best solution from submissions (36 ms).
    S = S.upper().replace('-', '')
    n = len(S)
    head = n % K
    res = [S[:head]] if head else []
    for i in range(head, n, K):
        res.append(S[i:i+K])
    return '-'.join(res)   # *** knowldge: linking list elements is faster.


print(licenseKeyFormatting("5F3Z-2e-9-w", 4))  # "5F3Z-2E9W"
print(licenseKeyFormatting("2-5g-3-J", 2))  # "2-5G-3J"
