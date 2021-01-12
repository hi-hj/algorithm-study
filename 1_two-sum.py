
# Brute Force
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# in 을 이용한 탐색
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i, n in enumerate(nums):
            complement = target - n
            
            if complement in nums[i+1:]:
                return nums.index(n), nums.index(complement)
            