# 다시 공부하기 (21.05.04)
import sys
sys.setrecursionlimit(30000)
from collections import defaultdict
answer = 0

def solution(a, edges):
    if sum(a)!=0:
        return -1
    
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    print(graph)
    def dfs(u, v):
        
        global answer
        print('****')
        print(u,v, answer)
        print(a)
        for node in graph[u]:
            print(node)
            if node!=v:
                dfs(node, u)
        answer += abs(a[u])
        a[v] += a[u]
        a[u] = 0
        
    dfs(0,0)
    return answer