from time import perf_counter

"""
https://leetcode.com/problems/reverse-words-in-a-string-iii/

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:

Input: s = "God Ding"
Output: "doG gniD"

Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([word[::-1] for word in s.split(" ")])


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.reverseWords("Let's take LeetCode contest")
    print(s1)
    assert s1 == "s'teL ekat edoCteeL tsetnoc"
    s2 = solution.reverseWords("God Ding")
    print(s2)
    assert s2 == "doG gniD"

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
