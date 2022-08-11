from typing import List
class Solution:
    def removeElement(self, nums:List[int], val:int) -> int:
        pt = len(nums)
        for i in range(len(nums)-1,-1,-1):
            #print(f'i = {i}')
            if nums[i] == val:
                #print(f'In i = {i}, had match!')
                del nums[i]
                nums.append(val)
                #print(nums)
                pt -= 1
        return pt

#Validating the code
nums = [0,1,2,2,3,0,4,2]
val = 2
c = Solution()
print(c.removeElement(nums, val))
print(nums)

nums = [3,2,2,3]
val = 3
c = Solution()
print(c.removeElement(nums, val))
print(nums)
