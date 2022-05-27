#Check if the order of brackets are correct: for example "(}]]" is False, and "(){}[]" is correct
#Also, "(({}))" and "{[()]}" are also crrect

class Solution:
    def isValid(self, s: str) -> bool:

        # Creating groups of Open Brackets:
        openbrack = ['(', '{', '[']

        auxlist = []
        for i in range(0, len(s)):

            if s[i] in openbrack:
                auxlist.append(s[i])
            else:

                try:
                    if (s[i] == ')' and auxlist[-1] == '(') or \
                            (s[i] == '}' and auxlist[-1] == '{') or \
                            (s[i] == ']' and auxlist[-1] == '['):

                        auxlist.pop()

                    else:
                        return False
                        break
                except:

                    return False

        if len(auxlist) == 0:
            return True
        else:
            return False


# ------------------------------------------------------------------------------------------------------------------------
c = Solution()
s = "[()]"

print(f'Testing the code: for s = {s}, the answer is: {c.isValid(s)}')