import sys
from collections import defaultdict, deque

def calc_graph(n, graph):
    visited = set()
    queue =deque()
    
    queue.append(1)
    visited.add(1)
    length = 1
    
    while queue:
        now = queue.popleft()
        
        for can_go in graph[now]:
            if can_go not in visited:
                visited.add(can_go)
                queue.append(can_go)
                length+=1
    
    return (n-length, length)


def solution(n, wires):
    answer = []
    graph = defaultdict(list)
    # 1. Setting
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    # 2. Run Function
    for a,b in wires:
        graph[a].remove(b)
        graph[b].remove(a)

        answer.append(calc_graph(n, graph))

        graph[a].append(b)
        graph[b].append(a)

    real_answer = sys.maxsize
    
    for a, b in answer:
        real_answer = min(real_answer, abs(a-b))
    return real_answer