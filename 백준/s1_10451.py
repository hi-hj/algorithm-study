import sys
input = sys.stdin.readline

import collections



def dfs(i, path):
    if i in path:
        return
    path.append(i)
    i = graph[i].pop(0)
    dfs(i, path)

test_case = int(input())
for _ in range(test_case):
    n = int(input())
    graph = collections.defaultdict(list)
    row = list(map(int, input().split()))

    for i in range(n):
        graph[i+1].append(row[i])
    cnt = 0

    for i in range(n):
        if graph[i+1]:
            dfs(i+1, [])
            cnt +=1
    
    print(cnt)

