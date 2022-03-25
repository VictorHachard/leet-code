from time import perf_counter

"""
https://leetcode.com/problems/regular-expression-matching/

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Constraints:

1 <= s.length <= 20
1 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        if '*' not in p and '.' not in p:
            return s == p
        if '*' in p and '.' not in p:
            p = p.replace('*', '')
            p *= len(s) // len(p)
            print(p, s)
            return s == p

        # Recursive solution needed


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.isMatch("aa", "a")
    print(s1)
    assert not s1
    s2 = solution.isMatch("aa", "a*")
    print(s2)
    assert s2
    s3 = solution.isMatch("ab", ".*")
    print(s3)
    assert s3

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
