#You are given a binary string s and a positive integer k.
#Return the length of the longest subsequence of s that makes up a binary number less than or equal to k.

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        end, n = len(s) - 1, s.count("0")
        while end >= 0 and int(s[end:], 2) <= k:
            end -= 1
        print(end)
        print(int(s[end:], 2))
        return n + s[end + 1:].count("1")

#Validation
s = "1001010"
k = 5
c = Solution()
print(f'Solution to s = {s} and k = {k}: {c.longestSubsequence(s,k)}')

s = "10010100000"
k = 1
print(f'Solution to s = {s} and k = {k}: {c.longestSubsequence(s,k)}')
s = "001010000"
s = s[1:]
print(int(s,2))