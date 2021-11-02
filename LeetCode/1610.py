import math

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, l: List[int]) -> int:
        
        array = []
        same = 0
        
        for p in points:
            if p == l:
                same+=1
            else:
                array.append(math.degrees(atan2(p[1]-l[1], p[0]-l[0])))
        array.sort()
        angles = array + [a + 360 for a in array]
        
        left, maxm = 0,0
        for right, a in enumerate(angles):
            if a - angles[left] > angle:
                left+=1
            maxm = max(maxm, right-left+1)
        
        return maxm+same