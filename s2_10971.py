# import sys
# input = sys.stdin.readline
# import copy
# sys.setrecursionlimit(1000)


# n = int(input())
# graph = [list(map(int, input().split())) for _ in range(n)]

# min_cnt = sys.maxsize

# def dfs(path, now, cnt):
#     global min_cnt
#     if cnt > min_cnt:
#         return

#     if len(path)==n:
#         if graph[now][path[0]]!= 0:
#             min_cnt = min(min_cnt, cnt + graph[now][path[0]])
#        # print(path, min_cnt)
#         return

#     for i in range(n):
#         if graph[now][i]!=0 and (i not in path):
#             cnt += graph[now][i]
#             path.append(i)
#             dfs(path, i, cnt)
#             path.pop()


# for i in range(n):
#     dfs([i], i, 0)

# print(min_cnt)

import sys


def dfs(start, next, value, visited):
    global min_value

    if len(visited) == N:
        if travel[next][start] != 0:
            min_value = min(min_value, value + travel[next][start])
        print(visited, value)
        return

    for i in range(N):
        if travel[next][i] != 0 and i != start and i not in visited:
            visited.append(i)
            dfs(start, i, value + travel[next][i], visited)
            visited.pop()


if __name__ == "__main__":

    N = int(input())
    travel = [list(map(int, input().split())) for _ in range(N)]

    min_value = sys.maxsize

    # 각 번호에서 시작
    for i in range(N):
        dfs(i, i, 0, [i])

    print(min_value)