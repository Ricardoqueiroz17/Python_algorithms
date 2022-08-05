from typing import List,Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return '[%s, %r, %r]' % (self.val, self.left, self.right)

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        mid = len(nums)//2
        return TreeNode(nums[mid],
                        self.sortedArrayToBST(nums[:mid]),
                        self.sortedArrayToBST(nums[mid+1:]))

#Valid
nums = [-10,-9,-8,-7,-3,0,5,9,10,11,13]
c = Solution()
print(c.sortedArrayToBST(nums))
