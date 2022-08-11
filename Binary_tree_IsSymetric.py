"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         # Method to show the TreeNode in the results

    def __repr__(self) -> str:
        return '[%s, %r, %r]' % (self.val, self.left, self.right)


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(p, q):

            if p and q:
                if p.val != q.val:
                    return False
                else:
                    return check(p.left, q.right) and check(p.right, q.left)
            else:
                if p:
                    return False
                if q:
                    return False
                return True

        return check(root.left, root.right)


#==============================================================================
# This is a complex validation, as long as we have to build a whole TreeNode with all its lefts and rights
#VALID 1
# Binary Tree we want to build =  [1,2,2,3,4,4,3] -> The result should be True

r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(2)

r.left.left = TreeNode(3)
r.left.right = TreeNode(4)

r.right.left = TreeNode(4)
r.right.right = TreeNode(3)

c = Solution()
print(c.isSymmetric(r))
#==============================================================================
#VALID 2
#Binary Tree we want to build = [1,2,2,None,3,None,3] -> The result should be False
r2 = TreeNode(1)
r2.left = TreeNode(2)
r2.right = TreeNode(2)

r2.left.left = TreeNode(None)
r2.left.right = TreeNode(3)

r2.right.left = TreeNode(None)
r2.right.right = TreeNode(3)

c2 = Solution()
print(c2.isSymmetric(r2))