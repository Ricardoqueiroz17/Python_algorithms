"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0,right=None,left=None):
        self.val=val
        self.right=right

    # Method to show the TreeNode in the results
    def __repr__(self) -> str:
        return '[%s, %r, %r]' % (self.val, self.left, self.right)


class Solution:
    def isSameTree(self, p:Optional[TreeNode], q:Optional[TreeNode])-> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

#Valid
a = TreeNode([1,2,3])
b = TreeNode([1,2,3])
c = Solution()
print(c.isSameTree(a,b))
