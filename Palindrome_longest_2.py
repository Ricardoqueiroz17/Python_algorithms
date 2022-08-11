class Solution:
    def longestPalindrome(self, s: str)-> str:

# ------First case: all elements are equal---------------------------------------------------------------------------------------
        all_eq = True
        for z in range(0,len(s)):
            if s[z] != s[0]:
                all_eq = False
                break
        if all_eq == True:
            return s

#-------Other cases 01 = sem letra do meio ex aabb --------------------------------------------------------------------------------------
        #print('------case 01--------------')
        stratual01 = ''
        max01 = ''
        for i in range(1, len(s)):
            #print(f' i = {i}')
            inf = i-1
            #print(f'inf = {inf}')
            j = 0
            while s[inf-j] == s[i+j]:
                #print(f'j = {j}')
                stratual01 = s[inf - j:i + j + 1]
                #print(f'j={j} and s = {s[inf - j]} == {s[i + j]}\n stratual = {stratual01}')
                if len(stratual01) > len(max01):
                    max01 = stratual01

                j += 1
                if inf - j < 0 or i+j >= len(s):
                    #print(f'Deu break!')
                    break

#-------Other cases 02 = com letra do meio (str com numero de elementos impar ex cabac --------------------------------------------------------------------------------------
        #print('------case 02--------------')
        stratual02 = ''
        max02 = ''
        for i in range(1, len(s)):
            j = 0
            while s[i - j] == s[i + j]:
                #print(f'j={j} and s = {s[i - j]} == {s[i + j]}')
                stratual02 = s[i-j:i+j+1]
                #print(f'j={j} and s = {s[inf - j]} == {s[i + j]}\n stratual02 = {stratual02} \n Max02 = {max02}')
                if len(stratual02) > len(max02):
                    max02 = stratual02

                j += 1
                if inf - j < 0 or i + j >= len(s):
                    break


        if len(max01) > len(max02):
            return max01
        else:
            return max02

#validation
c = Solution()
s = "adam"

print(c.longestPalindrome(s))


'''
s = "adam"
print(c.longestPalindrome(s))
'''
