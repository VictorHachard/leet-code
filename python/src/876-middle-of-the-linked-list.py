from time import perf_counter
from typing import Optional

"""
https://leetcode.com/problems/middle-of-the-linked-list/

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Stolen solution from leetcode
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
    print(s1)
    # assert s1 == ListNode(3, ListNode(4, ListNode(5)))
    s2 = solution.middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    print(s2)
    # assert s2 == ListNode(4, ListNode(5, ListNode(6)))

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
