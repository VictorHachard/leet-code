from time import perf_counter

"""
https://leetcode.com/problems/string-to-integer-atoi/

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi 
function). 

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'.
Read this character in if it is either. This determines if the final result is negative or positive 
respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the
string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0.
Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in
the range. Specifically, integers less than -231 should be clamped to -231, 
and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result. Note: 

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

Example 1:

Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.
Example 2:

Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.

Example 3:

Input: s = "4193 with words"
Output: 4193
Explanation:
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-231, 231 - 1], the final result is 4193.

Constraints:

0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
"""


class Solution:
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31

    def myAtoi(self, s: str) -> int:
        number = ''
        signe = '+'
        s = s.lstrip()  # remove leading whitespace

        for i in range(len(s)):
            # if the current character is a digit
            if s[i].isdigit():
                number += s[i]
            # if the current character is a sign and the next character is a digit and the number is empty
            elif len(number) == 0 and (s[i] == '-' or s[i] == '+') and i + 1 < len(s) and s[i + 1].isdigit():
                signe = s[i]
            else:
                break

        if number != '':
            number = int(signe + number)
            if number > self.INT_MAX:
                number = self.INT_MAX
            elif number < self.INT_MIN:
                number = self.INT_MIN
        else:
            number = 0
        return number


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.myAtoi("42")
    print(s1)
    assert s1 == 42
    s2 = solution.myAtoi("   -42")
    print(s2)
    assert s2 == -42
    s3 = solution.myAtoi("4193 with words")
    print(s3)
    assert s3 == 4193

    s4 = solution.myAtoi("words and 987")
    print(s4)
    assert s4 == 0
    s5 = solution.myAtoi("-91283472332")
    print(s5)
    assert s5 == -2147483648
    s6 = solution.myAtoi("+1")
    print(s6)
    assert s6 == 1
    s7 = solution.myAtoi("+-2")
    print(s7)
    assert s7 == 0
    s8 = solution.myAtoi("+-2147483648")
    print(s8)
    assert s8 == 0
    s9 = solution.myAtoi("-+12")
    print(s9)
    assert s9 == 0
    s10 = solution.myAtoi("+")
    print(s10)
    assert s10 == 0
    s11 = solution.myAtoi("00000-42a1234")
    print(s11)
    assert s11 == 0

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
