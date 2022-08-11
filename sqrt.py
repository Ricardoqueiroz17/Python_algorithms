class Solution:
    def mySqrt(self, x:int)-> int:

        if x == 0:
            return 0
        if 0 < x < 3:
            return 1

        for i in range(1, x):
            if i * i > x:
                return i-1
                break
            elif i * i == x:
                return i
                break


#Validation
c = Solution()
x = 0
print(c.mySqrt(x))