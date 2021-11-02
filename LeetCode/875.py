import sys
import scipy.signal._arraytools

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        answer = sys.maxsize
        start = 1
        end = sys.maxsize
        
        while start<=end:
            
            mid = (start+end)//2
            count = 0
            
            for pile in piles:
                q,r = divmod(pile, mid)
                count += q
                if r>0:
                    count+=1
            
            if count <= h:
                answer = min(answer, mid)
                end = mid -1
            else:
                start = mid+1
        
        return answer