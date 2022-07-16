"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

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

#Valid
c = Solution()
root = [12323232332,2,242424,2320392032,3,0,3]
print(c.isSymmetric(root))