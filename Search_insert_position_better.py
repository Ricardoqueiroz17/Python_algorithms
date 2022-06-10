from typing import List
class Solution:
    def searchInsert_2(self, nums:List[int], target:int)->int:
        if target in nums:
            return nums.index(target)
        index = 0
        for elem in nums:
            if elem < target:
                index += 1
                if index == len(nums):
                    return index
            else:
                return index

#Validating
nums = [1,3,5,6]
target = -12
c = Solution()
print(c.searchInsert_2(nums,target))