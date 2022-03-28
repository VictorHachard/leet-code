from time import perf_counter
from typing import Optional

"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val}"


class Solution:
    # Stolen solution: https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/1164537/Short-and-Simple-One-Pass-Solution-w-Explanation-or-Beats-100-or-No-dummy-node-required!
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next

        return head


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
    print('---')
    while s1:
        print(s1)
        s1 = s1.next
    # assert s1 ==
    s2 = solution.removeNthFromEnd(ListNode(1), 1)
    print('---')
    while s2:
        print(s2)
        s2 = s2.next
    # assert s2 ==
    s3 = solution.removeNthFromEnd(ListNode(1, ListNode(2)), 1)
    print('---')
    while s3:
        print(s3)
        s3 = s3.next

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
