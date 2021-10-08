import sys
import pprint

def solution(n, s, a, b, fares):
    s,a,b = s-1, a-1, b-1

    cost = [[sys.maxsize]*n for _ in range(n)]
    for start, end, fare in fares:
        cost[start-1][end-1] = fare
        cost[end-1][start-1] = fare
    
    # Floyd
    for k in range(n):
        cost[k][k] = 0
        for i in range(n):
            for j in range(n):
                cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])
    
    min_cost = sys.maxsize

    for i in range(n):
        share = cost[s][i]
        splitA = cost[i][a]
        splitB = cost[i][b]
        min_cost = min(min_cost, share+splitA+splitB)
    min_cost = min(min_cost, cost[s][a]+cost[s][b])

    return min_cost


solution(6,4,6,2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
solution(7,3,4,1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])
solution(6,4,5,6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]])

# from heapq import heappop, heappush

# INF = int(1e9)
# graph = [[]]

# def preprocess(n, fares):
#     global graph
#     graph = [[] for i in range(n+1)]

#     for fare in fares:
#         src, dst, cost = fare[0], fare[1], fare[2]
#         graph[src].append([dst, cost])
#         graph[dst].append([src, cost])

# def dijkstra(src, dst):
#     global graph
#     n = len(graph)
#     table = [INF for i in range(n)]
#     table[src] = 0
#     pq = [[0, src]]

#     while pq:
#         w, x = heappop(pq)

#         if table[x] < w: continue

#         for item in graph[x]:
#             nx, ncost = item[0], item[1]
#             ncost += w
#             if ncost < table[nx]:
#                 table[nx] = ncost
#                 heappush(pq, [ncost, nx])
    
#     return table[dst]

# def solution(n, s, a, b, fares):
#     preprocess(n, fares)
#     cost = INF

#     for i in range(1, n+1):
#         cost = min(cost, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))
    
#     return cost
