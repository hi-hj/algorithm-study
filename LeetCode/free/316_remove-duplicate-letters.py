from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        s = Counter(s)
        print(s)

        s = list(set(s))
        s.sort()
        print(s)

        print(''.join(s))



s = "cbacdcbc"
Solution().removeDuplicateLetters(s)