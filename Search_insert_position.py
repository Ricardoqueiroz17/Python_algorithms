from typing import List
class Solution:
    def searchInsert(self, nums:List[int], target:int)-> int:
        if target < nums[0]:
            pos = 0
            return pos
            quit()
        if target > nums[-1]:
            pos = len(nums)
            return pos
            quit()
#-------------------------------------------------
        for i in range(len(nums)):
            if nums[i] < target and nums[i + 1] > target:
                pos = i + 1
            if nums[i] == target:
                pos = i
                break
        return pos

#Validating
nums = [1,3,5,6]
target = 19
c = Solution()
print(c.searchInsert(nums,target))