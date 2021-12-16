from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        
        # 1. Iterate Search : Left 
        while i>=0 and nums[i] <= nums[i+1]:
            i-=1
        
        # 2. Iterate Search : Right
        if i>=0:
            j = len(nums)-1
            while (nums[i]>=nums[j]):
                j-=1
        
        # 3. Swap Left, Right
        # 4. Reverse arrays
        if i!=-1:
            nums[i], nums[j] = nums[j], nums[i]
            nums[i+1:] = nums[:i:-1]
        # 5. Edge Case : Do not have next permutation
        else:
            nums.sort()
            