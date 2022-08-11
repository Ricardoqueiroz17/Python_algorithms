from typing import List
class Solution:
    def merge(self, nums1:List[int], m:int, nums2: List[int], n:int)-> None:
        nums1[m:] = nums2[:n]
        print(nums1)
        return nums1.sort()

c = Solution()
nums1 = [0]
m = 0
nums2 = [1,2,3]
n = 3

print(c.merge(nums1,m,nums2,n))