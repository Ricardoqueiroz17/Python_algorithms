import bisect
from typing import List

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        l = len(nums)
        listSums = [0]*(l+1)
        listq = []
        nums.sort()
        i = 0
        for n in range(0,l+1):
            listSums[i] = sum(nums[0:n])
            i+=1
        print(listSums)

        for q in queries:
            #print(f'query = {q}')
            bis = bisect.bisect(listSums, q) #Rightmost index to insert. If I wanted the leftmost, I should have used bisect.bisect_right
            listq.append(bis-1)

        return listq
#valid
c = Solution()
nums = [2,3,4,5]
queries = [1]

print(c.answerQueries(nums,queries))