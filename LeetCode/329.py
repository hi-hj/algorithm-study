from typing import List
from collections import heapq

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # 1. Set variables
        max_heap = []
        m, n = len(matrix[0]), len(matrix)
        matrix_path = [[0]*m for _ in range(n)]
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        max_length = 1
        
        # 2. Add to max_heap
        for i in range(n):
            for j in range(m):
                heapq.heappush(max_heap, (-matrix[i][j], i,j))
        
        # 3. Iterate max_heap
        # * Key : Memoizaion & Update 
        while max_heap:
            point, x, y = heapq.heappop(max_heap)
            
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0<=nx<n and 0<=ny<m and matrix[nx][ny]>(-point):
                    matrix_path[x][y] = max(matrix_path[x][y], matrix_path[nx][ny]+1)
                    max_length = max(max_length, matrix_path[x][y]+1)
        
        return max_length
        