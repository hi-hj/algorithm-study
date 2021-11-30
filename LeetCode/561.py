from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        answer = 0
        
        # 1. Ascending Sum
        for i in range(len(nums)//2):
            answer += min(nums[i*2],nums[i*2+1])
        
        # 2. Calc only even num
        for i in range(len(nums//2)):
            answer += nums[i*2]
        
        return answer

        # 3. Python Style
        return sum(sorted(nums)[::2])