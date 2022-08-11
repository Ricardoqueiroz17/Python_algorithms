# Given two integers num and k, consider a set of positive integers with the following properties:
#     The units digit of each integer is k.
#     The sum of the integers is num.
# Return the minimum possible size of such a set, or -1 if no such set exists.

class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        if k == 0:
            return 1 if num%10 == 0 else 0

        for n in range (1, min(num//k, 10)+1):
            if (num - n*k)%10 == 0:
                return n

        return -1

#Validating
num = 58
k = 9
c = Solution()
print(f'Valid with num={num} and k = {k}: {c.minimumNumbers(num,k)}')

num = 5
k = 1
c = Solution()
print(f'Valid with num={num} and k = {k}: {c.minimumNumbers(num,k)}')

num = 0
k = 7
c = Solution()
print(f'Valid with num={num} and k = {k}: {c.minimumNumbers(num,k)}')


