import sys
input = sys.stdin.readline

n = int(input())
numbers = [list(map(int, input().split())) for _ in range(n)]
vectors = [list(map(int, input().split())) for _ in range(n)]

dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, 1, 1, 1, 0 ,-1, -1, -1]

r, c = map(int, input().split())
r, c= r-1, c-1

answer = 0

def can_go(x, y):
    num = numbers[x][y]
    vec = vectors[x][y]
    go_list = []
    for i in range(1, n):
        nx = x + dx[vec]*i
        ny = y + dy[vec]*i
        if 0<=nx<n and 0<=ny<n and numbers[nx][ny]>num:
            go_list.append((nx, ny))
    return go_list


def back_track(cur_idx, now_xy):
    global answer
    x, y = now_xy
    can_move = can_go(x, y)
    # 더 갈 수 없을때 (False)
    if not can_move:
        answer = max(answer, cur_idx)
        return
    # 더 갈 수 있을 때
    for nx, ny in can_move:
        back_track(cur_idx+1, (nx, ny))

back_track(0, (r,c))
print(answer)