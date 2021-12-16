from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        frequent = Counter(nums)
        for key, value in frequent.most_common(k):
            answer.append(key)
            
        return answer