import sys
import heapq

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        
        answer = -sys.maxsize
        n = len(points)
        
        heap = []
        heapq.heappush(heap, (-points[0][1]+points[0][0], points[0][0])) # yi-xi / xi
        
        for j in range(1, n):
            xj, yj = points[j]
            
            while heap and xj-heap[0][1] > k:
                heapq.heappop(heap)
            
            if heap:
                diff_h, _ = heap[0]
                answer = max(answer, xj+yj-diff_h)
            
            heapq.heappush(heap, (-yj+xj, xj))
        
        return answer