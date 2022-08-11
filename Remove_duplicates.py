from typing import List
class Solution:
    def removeDuplicates(self, nums:List[int]) -> int:

        pt = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[pt]:
                nums[pt+1] = nums[i]
                pt += 1

        print(f'resposta')
        return pt + 1


#Testing the class
c = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(c.removeDuplicates(nums))

c = Solution()
nums = [1,1,2]
print(c.removeDuplicates(nums))