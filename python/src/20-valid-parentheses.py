from time import perf_counter

"""
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        parser = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        stack = []

        for i in range(0, len(s), 1):
            if s[i] in parser:
                stack.append(s[i])
            else:
                if len(stack) == 0 or parser[stack.pop()] != s[i]:
                    return False

        return len(stack) == 0


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.isValid("()")
    print(s1)
    assert s1
    s2 = solution.isValid("()[]{}")
    print(s2)
    assert s2
    s3 = solution.isValid("(]")
    print(s3)
    assert not s3

    s4 = solution.isValid("{[]}")
    print(s4)
    assert s4
    s5 = solution.isValid("(")
    print(s5)
    assert not s5

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
