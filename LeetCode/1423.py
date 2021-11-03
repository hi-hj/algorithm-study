class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        left, right = [0]*n, [0]*n
        left[0] = cardPoints[0]
        right[0] = cardPoints[-1]
        
        # 1. DP
        for i in range(1, n):
            left[i] = left[i-1] + cardPoints[i]
        for i in range(1, n):
            right[i] = right[i-1] + cardPoints[-i-1]
        
        answer = 0
        
        # ALL LEFT or ALL RIGHT
        answer = max(answer, left[k-1], right[k-1])
        
        for i in range(1, k):
            answer = max(answer, left[i-1]+right[k-i-1])
        
        return answer
        
            