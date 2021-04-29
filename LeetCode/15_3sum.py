# 2. Two pointer
# 유사 문제 더 풀어보기
class Solution(object):
    def threeSum(self, nums):
        results = []
        nums.sort()
        
        for i in range(len(nums)-2):
            # jump duplicate
            if i>0 and nums[i] == nums[i-1]:
                continue
            # set left / right
            left, right = i+1, len(nums)-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum<0:
                    left +=1
                elif sum>0:
                    right -=1
                else:
                    results.append((nums[i], nums[left], nums[right]))

                    while left < right and nums[left] == nums[left+1]:
                        left +=1
                    while left < right and nums[right] == nums[right-1]:
                        right -=1
                    left +=1
                    right -=1
        return results

# 1. Use 'combinations'
# Result O / Time Complexity X
# from itertools import combinations

# class Solution(object):
#     def threeSum(self, nums):
#         nums.sort()
#         can_make = list(combinations(nums,3))
#         can_make = list(set(can_make))
#         result = []
#         for num in can_make:
#             if sum(num) == 0:
#                 result.append(num)
#         return result

nums = [-1,0,1,2,-1,-4]
Solution().threeSum(nums)