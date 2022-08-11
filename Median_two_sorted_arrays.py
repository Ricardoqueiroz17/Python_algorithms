"""
Hard level
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
"""
from typing import List
class Solution:

    def findMedianSortedArrays(self, nums1:List[int],nums2:List[int])-> float:
        m = len(nums1)
        n = len(nums2)
        total = nums1 + nums2
        lt = m + n
        half = lt//2-1
        print(half)
        x = Solution.mergesort(self, total)
        print(x)
        if (m+n)%2 == 0:
            mediana = float((x[half]+x[half+1])/2)
        else:
            mediana = float(x[half+1])
        return mediana

    def mergesort(self, total):
        n = len(total)
        if n <= 1:
            return total
        L = Solution.mergesort(self, total[0:round(n/2)])
        R = Solution.mergesort(self, total[round(n/2):n])

        return Solution.merge(self, L,R)

    def merge(self, L:List[int],R:list[int])-> List[int]:
        i=0
        j=0
        newl =[]
        while i<len(L) and j<len(R):
            if L[i] < R[j]:
                newl.append(L[i])
                i += 1
            else:
                newl.append(R[j])
                j += 1
        while i < len(L):
            newl.append(L[i])
            i +=1
        while j < len(R):
            newl.append(R[j])
            j+=1
        return newl

#Valid:
nums1 = [1,2]
nums2 = [3]
c = Solution()
print(c.findMedianSortedArrays(nums1,nums2))