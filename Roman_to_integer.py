class Solution:
    def romanToInt(self, s:str)->int:
        new_number = []
        i = 0
        while i < len(s):
            # --------------------------------------------------------------------------------
            # Six instances where subtraction is used (e.g. IV = 4, XC = 90)
            if s[i] == "I":
                if i == len(s) - 1:  # If we are in the last loop
                    new_number.append(1)
                else:
                    if s[i + 1] == "V":
                        new_number.append(4)
                        i = i + 1
                    elif s[i + 1] == "X":
                        new_number.append(9)
                        i = i + 1
                    else:
                        new_number.append(1)

            elif s[i] == "X":
                if i == len(s) - 1:  # If we are in the last loop
                    new_number.append(10)
                else:
                    if s[i + 1] == "L":
                        new_number.append(40)
                        i = i + 1
                    elif s[i + 1] == "C":
                        new_number.append(90)
                        i = i + 1
                    else:
                        new_number.append(10)

            elif s[i] == "C":
                if i == len(s) - 1:  # If we are in the last loop
                    new_number.append(100)
                else:
                    if s[i + 1] == "D":
                        new_number.append(400)
                        i = i + 1
                    elif s[i + 1] == "M":
                        new_number.append(900)
                        i = i + 1
                    else:
                        new_number.append(100)

            # -------------------------------------------------------------------------------
            else:
                if s[i] == "V":
                    new_number.append(5)
                if s[i] == "L":
                    new_number.append(50)
                if s[i] == "D":
                    new_number.append(500)
                if s[i] == "M":
                    new_number.append(1000)

            i = i + 1

        return sum(new_number)

#Testing the code

c = Solution()
s = "MCMXCIV"
c = Solution()
print(f'The roman number is: {s}')
print(f'Solution to the problem: ', c.romanToInt(s))