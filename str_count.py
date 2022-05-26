class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")

print("Enter the number:")
n = int(input())
print(n)
z = Solution()
print(z.hammingWeight(n))

