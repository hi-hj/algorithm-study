from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        # 1. Stack : memorize person's index
        stack = []
        for index, seat in enumerate(seats):
            if seat==1:
                stack.append(index)
        max_distance = 0
        
        # 2. Iterate & Update : max distance
        for i in range(len(stack)-1):
            max_distance = max(max_distance, (stack[i+1]-stack[i])//2)
        
        # 3. Edge case
        # if first or last seats are empty
        if stack[0]!=0:
            max_distance = max(max_distance, stack[0])
        if stack[-1]!=len(seats)-1:
            max_distance = max(max_distance, len(seats)-1-stack[-1])

        return max_distance