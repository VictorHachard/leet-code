from time import perf_counter

"""
https://leetcode.com/problems/permutation-in-string/

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        reversed_s1 = s1[::-1]
        for i in range(len(s2)):
            if s2[i:i + len(s1)] == reversed_s1 or s2[i:i + len(s1)] == s1:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.checkInclusion("ab", "eidbaooo")
    print(s1)
    assert s1
    s2 = solution.checkInclusion("ab", "eidboaoo")
    print(s2)
    assert not s2

    s3 = solution.checkInclusion("adc", "dcda")
    print(s3)
    assert s3
    s4 = solution.checkInclusion("ab", "ab")
    print(s4)
    assert s4
    s5 = solution.checkInclusion("abc", "bbbca")
    print(s5)
    assert s5

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
