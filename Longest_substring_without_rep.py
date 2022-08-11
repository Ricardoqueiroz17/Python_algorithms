"""
Given a string s, find the length of the longest substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s:str)-> int:
        count1 = 0
        count2 = 0
        start = 0
        i = 0

        if len(s) == 0:
            return 0
        for i in range(0,len(s)):
            #print(f'---------------------------------------------')
            #print(f' i = {i}\n start={start}\n seq={s[start:i]}\ncount1={count1}\ncount2={count2}')
            if s[i] in s[start:i]:
                #print(f'REPETE!')
                ind = start + s[start:i].index(s[i])
                count2 = max(i-start, count2)
                count1 = 0
                start = ind + 1
                #print(f'ind={ind}\n start={start} count2={count2}')
            else:
                count1 += 1

        count2 = max(i+1 - start, count2)
        if count2 == 0:
            count2 = count1
        return count2
#Validating

c = Solution()
print(c.lengthOfLongestSubstring("abcabcbb"))
print(c.lengthOfLongestSubstring("bbbbb"))
print(c.lengthOfLongestSubstring("pwwkew"))
