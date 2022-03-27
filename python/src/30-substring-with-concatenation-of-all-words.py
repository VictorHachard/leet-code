from time import perf_counter
from typing import List

"""
https://leetcode.com/problems/substring-with-concatenation-of-all-words/

You are given a string s and an array of strings words of the same length. Return all starting indices of substring(
s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening 
characters. 

You can return the answer in any order. 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]

Constraints:

1 <= s.length <= 104
s consists of lower-case English letters.
1 <= words.length <= 5000
1 <= words[i].length <= 30
words[i] consists of lower-case English letters.
"""


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        pass


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.findSubstring("barfoothefoobarman", ["foo", "bar"])
    print(s1)
    assert s1 == [0, 9]
    s2 = solution.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"])
    print(s2)
    assert s2 == []
    s3 = solution.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"])
    print(s3)
    assert s3 == [6, 9, 12]

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
