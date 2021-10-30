import heapq

class Solution:
    def minRefuelStops(self, target: int, tank: int, stations: List[List[int]]) -> int:
        pq = []
        stations.append((target, float('inf')))
        ans = prev = 0
        
        for location, capacity in stations:
            tank -= location - prev
            while pq and tank <0: # MUST REFUEL IN PAST
                tank += -heapq.heappop(pq)
                ans +=1

            if tank < 0 : return -1
            heapq.heappush(pq, -capacity)
            prev = location
            
        return ans
