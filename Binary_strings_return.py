class Solution:
    def addBinary(self, a: str, b: str)-> str:
        aint = int(a,2)
        bint = int(b,2)
        print(aint)
        print(bint)

        s = aint + bint
        print(s)
        sint = format(s,"b")
        return sint

c = Solution()
a = "11"
b = "1"
print(c.addBinary(a,b))