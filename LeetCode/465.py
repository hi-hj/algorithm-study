from collections import defaultdict, Counter
from typing import List
import heapq
import sys

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        
        balance = Counter()
        for f, t, a in transactions:
            balance[f]-=a
            balance[t]+=a

        balance = list(balance.values())
        return self.backtrack(balance, 0)

    def backtrack(self, arr, index):
        print(arr, index)
        if index == len(arr): return 0
        if not arr[index]:
            return self.backtrack(arr, index+1)
        
        min_txns = sys.maxsize
        for j in range(index+1, len(arr)):
            if (arr[j]*arr[index]) < 0:
                print(j)
                arr[j]+= arr[index]
                min_txns = min(1+self.backtrack(arr, index+1), min_txns)
                arr[j] -= arr[index]
        return min_txns




Solution().minTransfers([[0,1,10],[2,0,5]])
# Solution().minTransfers([[0,1,10],[1,0,1],[1,2,5],[2,0,5]])
# Solution().minTransfers([[10,11,6],[12,13,7],[14,15,2],[14,16,2],[14,17,2],[14,18,2]])