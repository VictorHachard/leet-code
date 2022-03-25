from time import perf_counter

"""
https://leetcode.com/problems/integer-to-roman/

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, 
which is simply X + II. The number 27 is written as XXVII, which is XX + V + II. 

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. 
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same 
principle applies to the number nine, which is written as IX. There are six instances where subtraction is used: 

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

Example 1:

Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.

Example 2:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 3:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:

1 <= num <= 3999
"""


class Solution:
    def intToRomanOld(self, num: int, roman: str = None) -> str:
        if roman is None:
            roman = ""
        roman_dict = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }
        if num == 0:
            return roman

        for key in sorted(roman_dict.keys(), reverse=True):
            if num >= key:
                return roman_dict[key] + self.intToRoman(num - key)

    # Stolen soltion: https://leetcode.com/problems/integer-to-roman/discuss/6273/Share-My-Python-Solution-96ms
    # Quicker than mine
    def intToRoman(self, num: int) -> str:
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num//1000] + C[(num % 1000)//100] + X[(num % 100)//10] + I[num % 10]


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.intToRoman(3)
    print(s1)
    assert s1 == "III"
    s2 = solution.intToRoman(58)
    print(s2)
    assert s2 == "LVIII"
    s3 = solution.intToRoman(1994)
    print(s3)
    assert s3 == "MCMXCIV"

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
