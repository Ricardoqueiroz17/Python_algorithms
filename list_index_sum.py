from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_list = []
        for i in range(len(nums)):
            for z in range(i + 1, len(nums)):
                if nums[i] + nums[z] == target:
                    new_list.append(i)
                    new_list.append(z)
                    break

        return new_list

z = Solution()
nums = [3,2,4]
target = 6
print(z.twoSum(nums, target))


