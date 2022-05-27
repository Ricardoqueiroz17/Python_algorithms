from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs[0] == "":
            return ""
        else:
            if len(strs) == 1:
                if strs[0] == "":
                    return ""
                else:
                    return strs[0]
            else:
                for i in range(0, 200):
                    if i > len(strs[0]):
                        return strs[0]
                        break
                    else:
                        result = False
                        new_list = [x[:i] for x in strs]
                        result = all(elem == new_list[0] for elem in new_list)
                        if result:
                            continue
                        else:
                            return new_list[0][:i - 1]
                            break

#Testing the code
strs = ["ab","a"]
c = Solution()
print(f'Answer = {c.longestCommonPrefix(strs)}')

strs = ["flower","flower","flower"]
c = Solution()
print(f'Answer = {c.longestCommonPrefix(strs)}')

strs = ["flower","flamba","fluor"]
c = Solution()
print(f'Answer = {c.longestCommonPrefix(strs)}')