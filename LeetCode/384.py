from typing import List
from itertools import permutations
import copy
import random

class Solution:
    
    
    def __init__(self, nums: List[int]):
        self.origin_array = copy.deepcopy(nums)
        self.nums = nums

    def reset(self) -> List[int]:
        return self.origin_array
        
    def shuffle(self) -> List[int]:
        random.shuffle(self.nums)
        return self.nums

sol = Solution([1,2,3])
print(sol.reset())
print(sol.shuffle())

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()