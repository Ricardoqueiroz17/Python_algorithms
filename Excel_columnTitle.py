"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
functions used:
Python chr() function is used to get a string representing of a character which points to a Unicode code integer.
For example, chr(97) returns the string 'a'. This function takes an integer argument and throws an error if it exceeds
from the specified range. The standard range of the argument is from 0 to 1,114,111.


"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        strlet = ''
        t = columnNumber
        i = 0
        while t > 0:
            #print(f'round = {i}')

            r = t % 26
            #print(f'r = {r}')
            if r == 0:
                letter = 'Z'
                t -= 26
            else:
                letter = chr(ord('A') + r - 1)
            #print(f'letter to be inserted = {letter}')
            strlet = ''.join((letter, strlet))

            t -= r
            #print(f'after i = {i}, coln = {t}')

            t //= 26
            #print(f'after first rest, t = {t}')
            i += 1

        return strlet

#Valid
columnNumber =704
c = Solution()
print(c.convertToTitle(columnNumber))
