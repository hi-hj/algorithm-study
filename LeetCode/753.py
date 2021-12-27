class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        
        # Example : n=2, k=3
        suffix_map = {} # 00:2
        all_combination = "0"*(n-1)
        if n == 1: return "".join(str(i) for i in range(k))
        if k == 1: return "0" * n
        
        
        for _ in range(k**n):
            suffix = all_combination[1-n:]
            suffix_map[suffix] = suffix_map.get(suffix, k)-1 # Next digit : k-1 -> k-2 -> k-3 -> .. 0
            all_combination += str(suffix_map[suffix]) # Add digit
        
        return all_combination