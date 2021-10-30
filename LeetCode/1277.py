from collections import defaultdict

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        # 1. Setting
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0]*m for _ in range(n)]
        count_square = defaultdict(int)
        dp[0] = matrix[0]
        answer = 0
        for i in range(n):
            dp[i][0] = matrix[i][0]
        
        # 2. DP
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j]==1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) +1
        
        for i in range(n):
            for j in range(m):
                if dp[i][j]!=0:
                    count_square[dp[i][j]]+=1
        
        for key, val in count_square.items():
            answer += (key*val)
        
        return answer
        
        