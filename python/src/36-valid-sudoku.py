from time import perf_counter
from typing import List

"""
https://leetcode.com/problems/valid-sudoku/

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in
the top left 3x3 sub-box, it is invalid. 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        found_row = set()
        found_col = set()
        found_3 = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if (str(i) + board[i][j]) in found_row or \
                            (str(j) + board[i][j]) in found_col or \
                            (str((i // 3) * 3 + (j // 3)) + board[i][j]) in found_3:
                        return False
                    else:
                        found_row.add(str(i) + board[i][j])
                        found_col.add(str(j) + board[i][j])
                        found_3.add(str((i // 3) * 3 + (j // 3)) + board[i][j])
        return True


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    print(solution.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                                  ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                                  [".", "9", "8", ".", ".", ".", ".", "6", "."],
                                  ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                                  ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                                  ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                                  [".", "6", ".", ".", ".", ".", "2", "8", "."],
                                  [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                                  [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
    print(solution.isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."],
                                  ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                                  [".", "9", "8", ".", ".", ".", ".", "6", "."],
                                  ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                                  ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                                  ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                                  [".", "6", ".", ".", ".", ".", "2", "8", "."],
                                  [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                                  [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

    print(solution.isValidSudoku([[".", ".", ".", ".", "5", ".", ".", "1", "."],
                                  [".", "4", ".", "3", ".", ".", ".", ".", "."],
                                  [".", ".", ".", ".", ".", "3", ".", ".", "1"],
                                  ["8", ".", ".", ".", ".", ".", ".", "2", "."],
                                  [".", ".", "2", ".", "7", ".", ".", ".", "."],
                                  [".", "1", "5", ".", ".", ".", ".", ".", "."],
                                  [".", ".", ".", ".", ".", "2", ".", ".", "."],
                                  [".", "2", ".", "9", ".", ".", ".", ".", "."],
                                  [".", ".", "4", ".", ".", ".", ".", ".", "."]]))

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
