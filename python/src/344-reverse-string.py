from time import perf_counter
from typing import List

"""
https://leetcode.com/problems/reverse-string/

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()  # Is the same as s[:] = s[::-1]

    def reverseString2(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            s[i], s[-i - 1] = s[-i - 1], s[i]


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = ["h", "e", "l", "l", "o"]
    solution.reverseString(s1)
    print(s1)
    assert s1 == ["o", "l", "l", "e", "h"]
    s2 = ["H", "a", "n", "n", "a", "h"]
    solution.reverseString(s2)
    print(s2)
    assert s2 == ["h", "a", "n", "n", "a", "H"]

    s1 = ["h", "e", "l", "l", "o"]
    solution.reverseString2(s1)
    print(s1)
    assert s1 == ["o", "l", "l", "e", "h"]
    s2 = ["H", "a", "n", "n", "a", "h"]
    solution.reverseString2(s2)
    print(s2)
    assert s2 == ["h", "a", "n", "n", "a", "H"]

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
