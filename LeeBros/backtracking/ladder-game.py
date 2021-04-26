import sys
n, m = map(int, input().split())

grid = [[0 for _ in range(n)] for _ in range(16)]
ladder_list = []


for _ in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    ladder_list.append((b, a))


def game(num, ladder):
    x, y = 0, num-1
    grid[x][y] = num
    visited = [[False]*n for _ in range(16)]
    visited[x][y] = True

    while x < 16:
        if (x, y) in ladder and visited[x][y+1]==False: y = y+1
        elif (x, y-1) in ladder and visited[x][y-1]==False: y = y-1
        else:
            x = x+1
            if x == 16: break
        if x ==15:
            grid[x][y] = num
        visited[x][y] = True

for i in range(1, n+1):
    game(i, ladder_list)
result = grid[15]
answer = []


def back_track(cur_idx, cur_list):
    global result, answer
    if cur_idx == m:
        grid[15] = [0 for _ in range(n)]
        for i in range(1, n+1):
            game(i, cur_list)
        compare_result = grid[15]
        # print(result, compare_result, len(cur_list))
        if result == compare_result:
            answer.append(len(cur_list))
        return
    
    back_track(cur_idx+1, cur_list)
    cur_list.append(ladder_list[cur_idx])
    back_track(cur_idx+1, cur_list)
    cur_list.pop()

back_track(0, [])

print(min(answer))