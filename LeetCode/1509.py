class Solution:
    def minDifference(self, nums):
        if len(nums) <= 4: return 0
        nums.sort()
        
        c1 = nums[-1] - nums[3]
        c2 = nums[-2] - nums[2]
        c3 = nums[-3] - nums[1]
        c4 = nums[-4] - nums[0]
        
        return min(c1,c2,c3,c4)