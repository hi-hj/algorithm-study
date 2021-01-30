N, M, V = map(int, input().split())

graph = {}
bfs_graph = {}

for i in range(N):
    graph[i+1] = []
    bfs_graph[i+1] = []
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    bfs_graph[a].append(b)

dfs_path = []
bfs_path = []

def dfs(start):
    global dfs_path
    if len(dfs_path)==N:
        return
    dfs_path.append(start)
    while graph[start]:
        dfs(graph[start].pop(0))


def bfs(start):
    queue = [start]
    visited = [start]
    while queue:
        vi = queue.pop(0)

        for i in bfs_graph[vi]:
            if i not in visited:
                queue.append(i)
                visited.append(i)
    return visited


dfs(V)
bfs_path = bfs(V)


for i in dfs_path:
    print(i, end=' ')
print()
for i in bfs_path:
    print(i, end=' ')


# def dfs(v):
#     print(v, end=' ')
#     visit[v] = 1
#     for i in range(1, n + 1):
#         if visit[i] == 0 and s[v][i] == 1:
#             dfs(i)

# def bfs(v):
#     queue = [v]
#     visit[v] = 0
#     while(queue):
#         v = queue[0]
#         print(v, end=' ')
#         del queue[0]
#         for i in range(1, n + 1):
#             if visit[i] == 1 and s[v][i] == 1:
#                 queue.append(i)
#                 visit[i] = 0

# n, m, v = map(int, input().split())
# s = [[0] * (n + 1) for i in range(n + 1)]
# visit = [0 for i in range(n + 1)]
# for i in range(m):
#     x, y = map(int, input().split())
#     s[x][y] = 1
#     s[y][x] = 1
    
# dfs(v)
# print()
# bfs(v)