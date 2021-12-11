class Solution:
    def isValid(self, string: str) -> bool:
        brackets = {
            ')':'(',
            '}':'{',
            ']':'['
            }
        stack = []
        
        for s in string:
            # print(s, stack)
            if (not stack) or (s not in brackets):
                stack.append(s)
            elif brackets[s] == stack[-1]:
                stack.pop()
            else:
                return False

        if not stack:
            return True
        else:
            return False


        # 2. Clean Code
        brackets = {')':'(', '}':'{',']':'['}
        stack = []
        
        for s in string:
            if s not in brackets:
                stack.append(s)
            elif not stack or brackets[s] != stack.pop():
                return False
        
        return len(stack)==0
