from typing import List
import bisect


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        result = []
        # 1. Erase out of boundary
        nums = nums[bisect.bisect_left(nums, lower):bisect.bisect_left(nums, upper+1)]
        
        # 2. Add Lower & Upper
        # to calc easily
        nums = [lower-1] + nums
        nums.append(upper+1)
        
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]+2:
                result.append(str(nums[i]+1) + "->" + str(nums[i+1]-1))
            elif nums[i+1] == nums[i]+1:
                continue
            elif nums[i+1] == nums[i]+2:
                result.append(str(nums[i]+1))
        return result
