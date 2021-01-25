import sys
input = sys.stdin.readline
import collections

m, n = map(int, input().split())
factory = [list(map(int, input().split())) for _ in range(m)]

def minus(a):
    a = int(a)
    return a-1

x1, y1, d1 = map(minus, input().split())
x2, y2, d2 = map(minus, input().split())

dx = [0,


def bfs(x1, y1, d1):
    queue = collections.deque()
    queue.append((x1, y1, d1))
    visited =[[[0]*4 for _ in range(n)] for _ in range(m)]
    visited[x1][y1][d1] = -1

    while queue:
        x, y, d = queue.popleft()
        
        
        for i in range(12):

