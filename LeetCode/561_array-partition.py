class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        sum = 0       
        for i, v in enumerate(nums):
            
            if i%2 == 0:
                sum += v
        return sum



class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        return sum(sorted(nums)[::2])