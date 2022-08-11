from typing import List
class Solution:
    def plusOne(self,  digits:List[int])->List[int]:
        for i in range(len(digits)-1,-1,-1):
            #print(f'first loop, i = {i}')
            while digits[i]+1 > 9:
                #print(f'dig position {i}')
                digits[i] = 0
                #print(f'digit after adding 1: {digits}')
                if i == 0:
                    #print(f'we are in the first element of digit')
                    digits.insert(0, 1)
                    #print(f'digit after finishing: {digits}')
                    return digits
                    exit()
                else:
                    i -= 1
                    continue
            #print(f'Exit the first loop, now the second. i ={i} and digits = {digits}')
            if i >= 0:
                digits[i] += 1
                break
        return digits

#Validating
digits = [0]
c = Solution()
print(c.plusOne(digits))
