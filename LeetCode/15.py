from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answers = []
        nums.sort()

        # Two Pointer
        # Two Sum : O(n) -> Three Sum : O(n**2)

        for i in range(len(nums)-2):
            if nums[i]==nums[i-1]:
                continue
            
            left, right = i+1, len(nums)-1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left+=1
                elif sum > 0:
                    right-=1
                else:
                    answers.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left]==nums[left+1]:
                        left+=1
                    while left < right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right+=1
        
        
        return answers
        

Solution.threeSum([-1,0,1,2,-1,-4])