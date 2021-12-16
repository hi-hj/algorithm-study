from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        char_dict = defaultdict(int)
        formed = 0
        left, right = 0,0
        answer = (right-left+1, left, right)

        
        if len(s)<=2:
            return len(s)
        
        while right < len(s):
            char = s[right]
            char_dict[char]+=1
            
            if char_dict[char]==1:
                formed+=1
            
            while left<=right and formed==3:
                char = s[left]
                char_dict[char]-=1
                if char_dict[char]==0:
                    formed-=1
                left+=1
            
            if right-left+1 > answer[0] and formed<=2:
                answer = (right-left+1, left, right)
            right+=1
        
        return answer[2]-answer[1] +1