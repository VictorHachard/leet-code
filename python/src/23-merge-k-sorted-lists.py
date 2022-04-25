from queue import PriorityQueue
from time import perf_counter
from typing import List, Optional

"""
https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    ListNode.__eq__ = lambda self, other: self.val == other.val
    ListNode.__lt__ = lambda self, other: self.val < other.val

    # Stolen solution: https://leetcode.com/problems/merge-k-sorted-lists/discuss/465094/Problems-with-Python3-and-Multiple-Solutions
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = sentinel = ListNode(None)
        pq = PriorityQueue()
        for _list in lists:
            if _list:
                pq.put((_list.val, _list))

        while not pq.empty():
            val, node = pq.get()
            sentinel.next = ListNode(val)
            sentinel = sentinel.next
            node = node.next
            if node:
                pq.put((node.val, node))

        return head.next


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    # s1 = solution.mergeKLists([[1,4,5],[1,3,4],[2,6]])
    # print(s1)
    # assert s1 == 42
    # s2 = solution.mergeKLists("42")
    # print(s2)
    # assert s2 == 42

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
