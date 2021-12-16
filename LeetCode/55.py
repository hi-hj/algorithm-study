from typing import List
import heapq

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        heap = []
        heapq.heappush(heap, -nums[0]) # max heap
        
        for idx, num in enumerate(nums):
            if idx > -heap[0]:
                return False
            heapq.heappush(heap, -num-idx)
        
        return True