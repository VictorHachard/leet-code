from time import perf_counter
from typing import List

"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could 
represent. Return the answer in any order. 

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any 
letters. 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""
Output: []

Example 3:

Input: digits = "2"
Output: ["a","b","c"]

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        res = []
        for i in range(len(digits)):
            if i == 0:
                res = phone[digits[i]]
            else:
                res = [x + y for x in res for y in phone[digits[i]]]
        return res


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.letterCombinations("23")
    print(s1)
    assert s1 == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    s2 = solution.letterCombinations("")
    print(s2)
    assert s2 == []
    s2 = solution.letterCombinations("2")
    print(s2)
    assert s2 == ["a", "b", "c"]

    s3 = solution.letterCombinations("234")
    print(s3)
    assert s3 == ["adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi", "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi", "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"]

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
