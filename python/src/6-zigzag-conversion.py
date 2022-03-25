from time import perf_counter

"""
https://leetcode.com/problems/zigzag-conversion/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to 
display this pattern in a fixed font for better legibility) 

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        else:
            lines = [''] * numRows
            pattern = (2 * (numRows - 1))  # pattern length, the sequence restarts every 2 * (numRows - 1)
            for i in range(len(s)):
                mod = i % pattern  # modulo to get the index of the line
                line = mod if mod < numRows else (2 * numRows - mod - 2)  # vertical line else diagonal line
                lines[line] += s[i]
            return ''.join(lines)


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.convert('PAYPALISHIRING', 3)
    print(s1)
    assert s1 == 'PAHNAPLSIIGYIR'
    s2 = solution.convert('PAYPALISHIRING', 4)
    print(s2)
    assert s2 == 'PINALSIGYAHRPI'
    s3 = solution.convert('A', 1)
    print(s3)
    assert s3 == 'A'

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
