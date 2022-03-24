from time import perf_counter

"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:

-231 <= x <= 231 - 1

Follow up: Could you solve it without converting the integer to a string?
"""


class Solution:
    def isPalindromeString(self, x: int) -> bool:
        if x < 0:
            return False
        return True if int(str(x)[::-1]) == x else False

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        return self.reverseNumber(x, 0) == x

    def reverseNumber(self, x: int, dup_x: int) -> int:
        # print("x: {}, dup_x: {}".format(x, dup_x))
        if x == 0:
            return dup_x

        dup_x = (dup_x * 10) + (x % 10)

        return self.reverseNumber(x // 10, dup_x)


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    print(solution.isPalindrome(121))
    print(solution.isPalindrome(-121))
    print(solution.isPalindrome(10))

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
