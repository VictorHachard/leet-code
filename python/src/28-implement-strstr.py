from time import perf_counter

"""
https://leetcode.com/problems/implement-strstr/

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and
Java's indexOf().

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

Example 3:

Input: haystack = "", needle = ""
Output: 0

Constraints:

0 <= haystack.length, needle.length <= 5 * 104
haystack and needle consist of only lower-case English characters.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.strStr("hello", "ll")
    print(s1)
    assert s1 == 2
    s2 = solution.strStr("aaaaa", "bba")
    print(s2)
    assert s2 == -1
    s3 = solution.strStr("", "")
    print(s3)
    assert s3 == 0

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
