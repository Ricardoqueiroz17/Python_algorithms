class Solution:
    def strStr(self,haystack:str, needle:str)-> int:
        if len(needle) == 0:
            return 0
        else:
            if needle in haystack:
                for i in range(len(haystack)):
                    if haystack[i] == needle[0]:
                        if len(needle) == 1:
                            return i
                            break
                        else:
                            for n in range(1,len(needle)):
                                #print(f'for n ={n}')
                                #print(f'init comparision: n={haystack[i+n]}')
                                if haystack[i+n] == needle[n]:
                                    if n == len(needle)-1:
                                        return i
                                        break
                                    else:
                                        continue
                                else:
                                    #print(f'Não deu ate o final!!')
                                    break
                return i


            else:
                return -1
#Validating
haystack = "mississippi"
needle = "issip"
c= Solution()
print(c.strStr(haystack, needle))

haystack = "aaa"
needle = "a"
c= Solution()

print(c.strStr(haystack, needle))