from collections import deque

class Solution:
    def calcString(self, string:deque) -> str:
        calc = ""
        while string:
            one = string.popleft()
            if one.isdigit():
                two = string.popleft()
                calc += int(one) * two
            else:
                calc += one
        
        return calc

    def decodeString(self, s: str) -> str:
        s = deque(s)
        stack = []
        # print(s)

        idx = -1

        while s:
            now = s.popleft()
            # print(stack, now)
            if now !=']':
                if now.isdigit():
                    while s[0].isdigit():
                        now+=s.popleft()
                stack.append(now)
            elif now ==']':
                temp = []
                idx = len(stack) - stack[::-1].index('[') -1
                calc = self.calcString(deque(stack[idx+1:]))
                # print(idx, calc)
                stack = stack[:idx]
                stack.append(calc)
        
        answer = self.calcString(deque(stack))
        print(answer)

        
        # d = deque(['a','b','c','3','d'])
        # print(self.calcString(d))
    

    
        # while s:
            

Solution().decodeString("100[leetcode]")
# Solution().decodeString("3[a2[c]]")
# Solution().decodeString("abc3[cd]xyz")