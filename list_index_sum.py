"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

from typing import List

#Best way: since we are dealing with indexes of list, its good to use the enumerate() method: enumerate(List) return two values: the index i and the value n in the i position
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = {}
        for i,n in enumerate(nums):
            if n in need: return [need[n], i]
            need[target-n] = i

#Other solution
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_list = []
        for i in range(len(nums)):
            for z in range(i + 1, len(nums)):
                if nums[i] + nums[z] == target:
                    new_list.append(i)
                    new_list.append(z)
                    break

        return new_list

z = Solution1()
nums = [3,2,4]
target = 6
print(z.twoSum(nums, target))


