class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        dots = []
        dots.append(p1), dots.append(p2), dots.append(p3), dots.append(p4)
        dist = []
        
        for i in range(3):
            for j in range(i+1, 4):
                dist.append(self.calc_dist(dots[i], dots[j]))
        
        dist = list(set(dist))
        dist.sort()
        
        if len(dist)==2 and dist[0]*2 ==dist[1]: return True
        else: return False

    def calc_dist(self, one,two):
        x = abs(one[0]-two[0])
        y = abs(one[1]-two[1])
        return x**2 + y**2