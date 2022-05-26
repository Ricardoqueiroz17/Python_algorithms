class Solution:
    def IsPalindrome(self, x: int) -> bool:
        s = str(x)
        if len(s) == 1:
            return True
        new_str = ""
        for i in range(len(s) - 1, -1, -1):
            new_str += s[i]

        if s == new_str:
            return True
        else:
            return False

z = Solution()
print(z.IsPalindrome(1233210))
