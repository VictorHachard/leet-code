import re
from time import perf_counter

"""
https://leetcode.com/problems/valid-number/

A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
One or more digits, followed by a dot '.'.
One or more digits, followed by a dot '.', followed by one or more digits.
A dot '.', followed by one or more digits.
An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One or more digits.
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7",
"+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5",
"--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

Example 1:

Input: s = "0"
Output: true

Example 2:

Input: s = "e"
Output: false

Example 3:

Input: s = "."
Output: false

Constraints:

1 <= s.length <= 20
s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.
"""


class Solution:
    def isNumber(self, s: str) -> bool:
        return bool(re.match(re.compile(r'^[+-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?$'), s))


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.isNumber("0")
    print(s1)
    assert s1
    s2 = solution.isNumber("e")
    print(s2)
    assert not s2
    s3 = solution.isNumber(".")
    print(s3)
    assert not s3

    s4 = solution.isNumber("-0.1")
    print(s4)
    assert s4
    s5 = solution.isNumber("+3.14")
    print(s5)
    assert s5
    s6 = solution.isNumber("4.")
    print(s6)
    assert s6
    s7 = solution.isNumber("-.9")
    print(s7)
    assert s7
    s8 = solution.isNumber("2e10")
    print(s8)
    assert s8
    s9 = solution.isNumber("-90E3")
    print(s9)
    assert s9
    s10 = solution.isNumber("3e+7")
    print(s10)
    assert s10
    s11 = solution.isNumber("+6e-1")
    print(s11)
    assert s11
    s12 = solution.isNumber("53.5e93")
    print(s12)
    assert s12

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
