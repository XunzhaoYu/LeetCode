from itertools import permutations, combinations
"""
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.

    top: 0011
    bottom: 011001

For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:
    Input: n = 1
    Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]

Note:
    The order of output does not matter.
    The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
    The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
"""


def readBinaryWatch(num: int) -> list:
    # 36 ms, faster than 92.20%.
    if num <= 0:
        return ["0:00"]

    retValue = []
    for leds in combinations(range(10), num):
        hour = 0
        minutes = 0
        for led in leds:
            if led < 4:
                hour |= 1 << led  # *** <<
            else:
                led = led - 4
                minutes |= 1 << led
        if hour > 12 or minutes > 59:
            continue
        elif hour == 12:
            continue
        else:
            timeStr = "{0}:{1}".format(hour, "0" + str(minutes) if minutes < 10 else str(minutes))
            retValue.append(timeStr)
    return retValue


def readBinaryWatch2(num: int) -> list:
        # 40 ms, faster than 68.21%. The best solution from submissions (32 ms.)
        return ['%d:%02d' % (h, m)  # *** 02d
                for h in range(12) for m in range(60)  # *** two for in []
                if (bin(h) + bin(m)).count('1') == num]


print(readBinaryWatch(2))
