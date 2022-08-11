class Solution:
    def lengthOfLastWord(self, s: str)-> int:
        x = s.split(" ")
        for i in range(len(x)-1,-1,-1):
            if len(x[i])>0:
                return len(x[i])
                break

        return 0

#Validating
c = Solution()
s = "luffy is still joyboy"
print(c.lengthOfLastWord(s))