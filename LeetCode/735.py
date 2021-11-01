class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for astr in asteroids:
            
            # 1. ADD
            if not stack \
                or stack[-1]>0 and astr>0 \
                or stack[-1]<0 and astr<0 \
                or stack[-1]<0 and astr>0:
                stack.append(astr)
                
            # 2. COLLISION!
            # -> vs <-
            else:
                stack.append(astr)
                while len(stack)>1 and (stack[-2]>0 and stack[-1]<0):
                    astr = stack.pop()
                    if stack[-1] > abs(astr):
                        break
                    elif stack[-1]==abs(astr):
                        stack.pop()
                        continue
                    elif stack[-1]<abs(astr):
                        stack.pop()
                        stack.append(astr)
                    astr = stack[-1]
                    
        return stack