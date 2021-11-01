import sys

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        start = 0
        end = 0
        n = len(nums)
        
        for i in range(n):
            end += nums[i]
            if start < nums[i]: start = nums[i]
        
        answer = end
        
        
        while start <=end:
            mid = (start + end)//2
            total = 0
            cnt = 1
            
            for i in range(n):
                if (total + nums[i] > mid):
                    cnt+=1
                    total = nums[i]
                else:
                    total +=nums[i]
            
            if cnt<=m:
                answer = min(answer, mid)
                end = mid -1
            else:
                start = mid+1
        
        return answer
            

Solution().splitArray([7,2,5,10,8],2)