from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # 1. Brute Force
        # O(n**2)
        # Time Out
        answer = 0
        for i in range(len(height)):
            left_max, right_max = 0,0
            for j in range(i):
                left_max = max(left_max, height[j])
            for j in range(i, len(height)):
                right_max = max(right_max, height[j])
            now = min(left_max, right_max) - height[i]
            if now>0:
                answer += now
        return answer
        
        # 2. DP
        # TC: O(n)
        # SC : O(n)
        answer = 0
        n = len(height)
        left, right = [0]*n, [0]*n
        left[0], right[-1] = height[0], height[-1]

        for i in range(1, n):
            left[i] = max(height[i], left[i-1])
        for i in range(n-2, -1, -1):
            right[i] = max(height[i], right[i+1])
        for i in range(1, n-1):
            answer += min(left[i], right[i]) - height[i]
        
        return answer

        # 3. Two Pointer
        # TC : O(n)
        # SC : O(n). No need additioanl array used in DP solution.
        answer = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
            
            if left_max <= right_max:
                answer += left_max-height[left]
                left+=1
            else:
                answer += right_max-height[right]
                right-=1
        return answer

Solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])