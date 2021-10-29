class Solution(object):
    def twoSum(self, nums, target):
        nums_map ={}
        for i, num in enumerate(nums):
            nums_map[num] = i

        for i, num in enumerate(nums):
            if target - num in nums_map and i!= nums_map[target-num]:
                return nums.index(num), nums_map[target-num]

nums = [2,7,11,15]
target = 9
Solution().twoSum(nums, target)

# # Brute Force
# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

# # in 을 이용한 탐색
# # 똑같은 O(n**2)이라도, in을 활용한 연산이 더 빠르다.*
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:

#         for i, n in enumerate(nums):
#             complement = target - n
            
#             if complement in nums[i+1:]:
#                 return nums.index(n), nums.index(complement)
            