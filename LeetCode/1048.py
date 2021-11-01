from collections import defaultdict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        
        chain_len = defaultdict()
        max_len = 0
        words.sort(key = len)
        for word in words:
            cur_len = 1
            
            for i in range(len(word)):
                now = word[:i] + word[i+1:]
                if now in chain_len:
                    cur_len = max(cur_len, chain_len[now]+1)
            
            chain_len[word] = cur_len
            
            max_len = max(max_len, cur_len)
        
        return max_len