from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # 1. Set
        count = 0
        jewels = set(jewels)
        
        for stone in stones:
            if stone in jewels:
                count+=1
        
        return count

        # 2. Counter
        freqs = Counter(jewels)
        count = 0
        for j in jewels:
            count += freqs[j]
        return count
        