from time import perf_counter
from typing import Optional

"""
https://leetcode.com/problems/merge-two-binary-trees/

You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others 
are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, 
then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of 
the new tree. 

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.

Example 1:

Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]

Example 2:

Input: root1 = [1], root2 = [1,2]
Output: [2,2]

Constraints:

The number of nodes in both trees is in the range [0, 2000].
-104 <= Node.val <= 104
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        string = str(self.val)
        if self.left:
            string += '(' + str(self.left) + ')'
        if self.right:
            string += '(' + str(self.right) + ')'
        return string

    # https://stackoverflow.com/questions/55707832/binary-tree-node
    def __eq__(self, other):
        return (self is None and other is None) \
               or (not ((self is None and other is not None) or (self is not None and other is None))) \
               or (self.val == other.val and self.left == other.left and self.right == other.right)


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            root = TreeNode(root1.val + root2.val)
            root.left = self.mergeTrees(root1.left, root2.left)
            root.right = self.mergeTrees(root1.right, root2.right)
            return root
        else:
            return root1 or root2


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.mergeTrees(TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2)), TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(4), TreeNode(7))))
    print(s1)
    assert s1 == TreeNode(3, TreeNode(4, TreeNode(5), TreeNode(5)), TreeNode(4, None, TreeNode(7)))
    s2 = solution.mergeTrees(TreeNode(1), TreeNode(1, TreeNode(2)))
    print(s2)
    assert s2 == TreeNode(2, TreeNode(2))

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
