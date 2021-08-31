from collections import defaultdict
import heapq
import sys

def solution(N, road, K):
    graph = defaultdict(list)

    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    def dijkstra(graph, start):
        max_num = 0
        distances = [sys.maxsize]*(N+1)
        distances[start] = 0

        queue = []
        heapq.heappush(queue, (0, start))
        
        while queue:
            weight, now = heapq.heappop(queue)
            
            if distances[now] < weight:
                continue
            for new_dest, new_weight in graph[now]:
                cost = weight + new_weight
                if cost < distances[new_dest]:
                    distances[new_dest] = cost
                    heapq.heappush(queue, (cost, new_dest))
        
        return distances
    
    answer = 0
    for num in dijkstra(graph, 1):
        if num<=K:
            answer +=1
    print(answer)
    return answer



solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)