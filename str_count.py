#Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")

print("Enter the number:")
n = int(input())
print(n)
z = Solution()
print(z.hammingWeight(n))

