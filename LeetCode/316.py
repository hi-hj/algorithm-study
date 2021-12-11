from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        count = Counter(s)
        seen = set()
        stack = []
        
        for char in s:
            count[char]-=1
            if char in seen:
                continue
            
            while stack and char < stack[-1] and count[stack[-1]]>0:
                seen.remove(stack.pop())
            seen.add(char)
            stack.append(char)

        return ''.join(stack)
            