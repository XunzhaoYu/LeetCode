"""
We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not.
The given string will always end with a zero.

Example 1:
    Input: bits = [1, 0, 0]
    Output: True
    Explanation: The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.

Example 2:
    Input: bits = [1, 1, 1, 0]
    Output: False
    Explanation: The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.

Note:
    1 <= len(bits) <= 1000.
    bits[i] is always 0 or 1.
"""

def isOneBitCharacter(bits: List[int]) -> bool:
    # 32 ms, faster than 96.84%.
    nb = len(bits)
    if bits[-1] == 1:
        return False
    for i in range(2, nb+1):
        if not bits[-i]:
            return i%2 == 0
    return (nb-1)%2 == 0


def isOneBitCharacter2(bits: List[int]) -> bool:
    # 36 ms, faster than 91.70%. The best solution from submissions (24 ms)
    i=0
    length=len(bits)-1
    while i<length:
        if bits[i]==1:
            i+=1
        i+=1
    return i==length
