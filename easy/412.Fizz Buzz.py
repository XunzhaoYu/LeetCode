"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

        n = 15,

        Return:
        [
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz"
        ]
"""


def fizzBuzz(n: int) -> List[str]:
    # 56 ms, faster than 73.04%. Better than the best solution from submissions (48 ms, tested to be 72 ms.)
    res = []
    for i in range(1, n + 1):
        if i % 3 == 0:
            if i % 5 == 0:
                res.append("FizzBuzz")
            else:
                res.append("Fizz")
        elif i % 5 == 0:
            res.append("Buzz")
        else:
            res.append(str(i))
    return res

