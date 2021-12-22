from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # distance = [(x**2+y**2, x,y) for x,y in points]
        # distance.sort()
        # distance = distance[:k]
        # answer = []
        # for _, x,y in distance:
        #     answer.append([x,y])
        # return answer
    
        points.sort(key = lambda x: x[0]**2 +x[1]**2)
        return points[:k]