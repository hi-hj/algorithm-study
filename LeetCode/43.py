class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = 0
        
        # 1. Brute Force
        for i in range(len(num1)):
            first_digit = len(num1) - i -1
            for j in range(len(num2)):
                second_digit = len(num2) - j -1
                result += int(num1[i])*int(num2[j])*10**(first_digit+second_digit)
        return str(result)
            
        
        
#         # 2. Use 'eval'
#         return str(eval(num1+"*"+num2))