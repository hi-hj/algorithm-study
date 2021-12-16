import sys
from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = Counter(t)
        sCount = defaultdict(int)
        required, formed = len(tCount), 0
        
        left,right = 0,0
        min_length = sys.maxsize
        answer = (sys.maxsize, None, None)
        
        
        while right < len(s):
            char = s[right]
            sCount[char]+=1
            
            if char in tCount and sCount[char]==tCount[char]:
                formed+=1
            
            while left <= right and formed == required:
                char = s[left]
                if right-left+1<answer[0]:
                    answer = (right-left+1, left, right)
                sCount[char]-=1
                if char in tCount and sCount[char]<tCount[char]:
                    formed-=1
                left+=1
            
            right+=1
        
        if answer[0]==sys.maxsize:
            return ""
        else:
            return s[answer[1]:answer[2]+1]