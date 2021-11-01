class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []
        for p, s in sorted(zip(position, speed), reverse= True):
            dist = target - p
            time = dist / s
            
            if not stack or time>stack[-1]:
                stack.append(time)
        
        return len(stack)