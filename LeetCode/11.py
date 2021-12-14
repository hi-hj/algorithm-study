from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 1. Brute Force
        max_area = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                max_area = max(max_area, min(height[i],height[j]) * (j-i))
        return max_area


        # 2. Two Pointer
        max_area = 0
        left, right = 0, len(height)-1

        while left < right:
            max_area = max(max_area, min(height[left],height[right]) * (right-left))
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        
        return max_area