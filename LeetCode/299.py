from typing import List
from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        n = len(secret)
        secret, guess = list(secret), list(guess)

        # 1. Count Bulls
        for i in range(n):
            if secret[i]==guess[i]:
                bulls+=1
                secret[i] = 'a'
                guess[i]='a'
        # 2. Count Cows
        secret = Counter(secret)
        guess = Counter(guess)

        for key, value in guess.items():
            if key =='a':
                continue
            if key in secret:
                cows += min(value, secret[key])
        
        return str(bulls)+"A"+str(cows)+"B"



Solution().getHint("1807","7810")
Solution().getHint("1123","0111")