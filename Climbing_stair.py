#You are climbing a staircase: n steps to reach the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways you can climb.
#Constrains = 1<=n<=45
class Solution:
    def climbStairs(self, n:int)-> int:
        #The solution will follow a fibonacci sequence
        f = []
        for i in range(0,n+2):
            f.append(0)
        f[0] = 0
        f[1] = 1
        print(f)
        for i in range(2,n+2):
            f[i] = f[i-1] + f[i-2]
        print(f)
        return f[-1]
#Validating
n = 3
c = Solution()
print(c.climbStairs(n))