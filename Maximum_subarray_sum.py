from typing import List
class Solution:
    def maxSubArray(self, nums:List[int])-> int:
        maxsum = float('-inf')
        currsum = 0
        for elem in nums:
            print(f'for element = {elem}')
            currsum = max(elem, currsum + elem)
            print(f'currentsum = {currsum}')
            maxsum = max(currsum, maxsum)
            print(f'MAX = {maxsum}')
        return maxsum

    def maxSubArray2(self, nums: List[int]) -> int:
        maxsum = float('-inf')
        curr = float('-inf')
        for n in nums:
            curr = max(n,curr+n)
            maxsum = max(curr,maxsum)
        return maxsum


#Validation
c = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(f'Answer: {c.maxSubArray2(nums)}')