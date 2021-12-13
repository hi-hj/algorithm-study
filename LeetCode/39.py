from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        
        candidates.sort()
        
        def dfs(elements, csum, index):
            if csum == target:
                results.append(elements[:])
                return
            
            for i in range(index, len(candidates)):
                if csum + candidates[i] <= target:
                    elements.append(candidates[i])
                    
                    dfs(elements, csum+candidates[i], i)
                    
                    elements.pop()
        
        dfs([], 0, 0)
        
        return results
        