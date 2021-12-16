from  typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # 1. Type Casting
        return list(str(int(''.join(map(str, digits))) + 1))
    

        # 2. Calc as Integer
        digits = [0] + digits  
        right = len(digits)-1
        
        #  ... 9,9,9
        if digits[right]==9:
            while digits[right]==9:
                digits[right] = 0
                right -=1
            digits[right]+=1
        else:
            digits[right]+=1
        
        if digits[0]==0:
            digits.pop(0)
        
        return digits
        