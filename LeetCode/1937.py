class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        m = len(points[0])
        answer = max(points[0])
        
        for i in range(1, n):
            dp = points[i-1]
            for right in range(1, m):
                dp[right] = max(dp[right], dp[right-1]-1)
            for left in range(m-2, -1, -1):
                dp[left] = max(dp[left], dp[left+1]-1)
            for j in range(m):
                points[i][j] += dp[j]
            answer = max(answer, max(points[i]))
        return answer
        
#         n = len(points)
#         m = len(points[0])
#         dp = [[0]*m for _ in range(n)]
        
#         dp[0] = points[0]
        
#         for i in range(1, n):
#             for j in range(m):
#                 for k in range(m):
#                     dp[i][j] = max(dp[i][j], points[i][j] + dp[i-1][k] - abs(j-k))
#         return max(dp[-1])