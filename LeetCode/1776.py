import sys

class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        result = []
        
        stack = []
        
        for p, s in cars[::-1]:
            
            # NOT COLLIDE
            # LOW SPEED
            while stack and (s <= stack[-1][1] or (stack[-1][0]-p)/(s-stack[-1][1]) >=stack[-1][2]):
                stack.pop()
            
            # NOT COLLIDE
            if not stack:
                stack.append((p,s,sys.maxsize))
                result.append(-1)
            # COLLIDE
            else:
                collide_time = (stack[-1][0]-p) / (s-stack[-1][1])
                stack.append((p,s,collide_time))
                result.append(collide_time)
        
        result.reverse()
        return result
        