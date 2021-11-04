from collections import Counter

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        count = Counter(changed)
        changed.sort()
        if len(changed)%2==1:
            return []
        
        answer = []
        
        for num in sorted(changed):
            if count[num] ==0: continue
            if count[num*2] ==0 : return []
            count[num]-=1
            count[num*2]-=1
            answer.append(num)
            
        return answer