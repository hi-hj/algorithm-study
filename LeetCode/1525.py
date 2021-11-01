from collections import defaultdict

class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        answer = 0
        s = list(s)
        one =defaultdict(int)
        two =defaultdict(int)
        for c in s: two[c]+=1
        
        one_num = 0
        two_num = 0
        for key, val in two.items():
            if val>0: two_num+=1
        
        for i in range(n):
            now = s[i]
            if one[now]==0:one_num+=1
            one[now]+=1
            if two[now]==1:two_num-=1
            two[now]-=1
            
            if one_num==two_num:answer+=1

        
        return answer