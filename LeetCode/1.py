from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. Brute Force
        # O(n**2)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        # 2. Using Dictionary
        # O(n)
        # not using same element is key
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i
        
        for i, num in enumerate(nums):
            if target-num in nums_map and i!=nums_map[target-num]:
                return [i, nums_map[target-num]]
        
        # 2-2. Clean Code
        # Two for loop -> One for loop
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [i, nums_map[target-num]]
            nums_map[num] = i

Solution.twoSum([3,2,4], 6)