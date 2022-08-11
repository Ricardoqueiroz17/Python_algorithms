"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right
 at any point in time. Given the two integers m and n, return the number of possible unique paths that the robot
 can take to reach the bottom-right corner.
"""
"""
This is a Dynamic Programming problem, with permutations.
"""

class Solution:
    def uniquePaths(self, m:int, n:int)-> int:

        #First, generate the matrix "m x n" with the nodes
        dp = [[0 for col in range(n)] for row in range(m)]

        def solve(row,col):
            if row == m-1 or col == n-1:
                return 1

            if dp[row][col] != 0:
                return dp[row][col]

            dp[row][col] = solve(row+1,col) + solve(row,col+1)
            return dp[row][col]

        return solve(0,0)



c = Solution()

print(c.uniquePaths(3,7))
