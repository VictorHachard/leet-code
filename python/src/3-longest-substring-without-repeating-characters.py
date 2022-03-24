from time import perf_counter

"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution(object):
    # First solution
    # def lengthOfLongestSubstring(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     if not s:
    #         return 0
    #
    #     max_len = 0
    #     temp_len = 1
    #     for i in range(len(s)):
    #         for j in range(i + 1, len(s)):
    #             if s[j] not in s[i:j]:
    #                 temp_len += 1
    #             else:
    #                 break
    #         max_len = max(max_len, temp_len)
    #         temp_len = 1
    #     return max_len

    # Stolen solution: https://redquark.org/leetcode/0003-longest-substring-without-repeating-characters/
    def lengthOfLongestSubstring(self, s):
        if not s or s == '':
            return 0

        start = 0
        end = 0
        max_length = 0
        unique_characters = set()

        while end < len(s):
            if s[end] not in unique_characters:
                unique_characters.add(s[end])
                end += 1
                max_length = max(max_length, len(unique_characters))
            else:
                unique_characters.remove(s[start])
                start += 1

        return max_length


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    print(solution.lengthOfLongestSubstring('abcabcbb'))
    print(solution.lengthOfLongestSubstring('bbbbb'))
    print(solution.lengthOfLongestSubstring('pwwkew'))

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
