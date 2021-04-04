BLANK = (-1, -1, -1)

# 변수 선언 및 입력:
n, m, k = tuple(map(int, input().split()))

mold = [
    [BLANK for _ in range(m)]
    for _ in range(n)
]
next_mold = [
    [BLANK for _ in range(m)]
    for _ in range(n)
]

ans = 0


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


def collect(col):
    global ans
    for row in range(n):
        if mold[row][col] != BLANK:
            mold_size, _, _ = mold[row][col]
            
            ans += mold_size
            mold[row][col] = BLANK
            break


def get_next_pos(x, y, dist, move_dir):
    # 문제에서 주어진 순서인 위, 아래, 오른쪽, 왼쪽 순으로 적어줍니다. 
    dxs, dys = [-1, 1, 0, 0], [0, 0, 1, -1]
    
    # dist번 한 칸씩 이동하면 됩니다.
    for _ in range(dist):
        next_x, next_y = x + dxs[move_dir], y + dys[move_dir]
        # 현재 방향으로 이동했다 했을 때
        # 만약 격자를 벗어나지 않는다면, 그대로 이동합니다.
        if in_range(next_x, next_y):
            x, y = next_x, next_y
        # 만약 격자를 벗어나게 된다면
        # 방향을 반대로 바꾸고 한 칸 이동하면 됩니다.
        else:
            move_dir = move_dir + 1 if move_dir % 2 == 0 else move_dir - 1
            x, y = x + dxs[move_dir], y + dys[move_dir]
    
    return (x, y, move_dir)


# (x, y) 위치에 있는 곰팡이를 이동시킵니다.
def move(x, y):
    mold_size, dist, move_dir = mold[x][y]
    next_x, next_y, next_dir = get_next_pos(x, y, dist, move_dir)
    
    new_mold = (mold_size, dist, next_dir)
    
    # 현재 곰팡이의 크기가 해당 위치에 있던 것 보다 더 큰 경우에만
    # 곰팡이 정보를 적어줍니다.
    # 그렇지 않은 경우라면 충돌시 사라지게 될 곰팡이이므로
    # 무시하면 됩니다.
    if new_mold > next_mold[next_x][next_y]:
        next_mold[next_x][next_y] = new_mold


def move_all():
    # next_mold 값을 전부 빈칸으로 초기화합니다.
    for i in range(n):
        for j in range(m):
            next_mold[i][j] = BLANK
    
    # 곰팡이를 한번씩 이동시킵니다.
    for i in range(n):
        for j in range(m):
            if mold[i][j] != BLANK:
                move(i, j)
    
    # next_mold 값을 mold에 옮겨줍니다.
    for i in range(n):
        for j in range(m):
            mold[i][j] = next_mold[i][j]


def simulate(col):
    # 해당 열에 있는 곰팡이를 채취합니다.
    collect(col)
    
    # 곰팡이들을 전부 움직입니다.
    move_all()

    
for _ in range(k):
    x, y, s, d, b = tuple(map(int, input().split()))
        
    # 위, 아래 방향으로 움직이는 경우
    # 2n - 2번 움직이면 다시 제자리로 돌아오게 되므로
    # 움직여야 할 거리를 2n - 2로 나눴을 때의 나머지 만큼만
    # 움직이게 하면 최적화가 가능합니다.
    if d <= 2:
        s %= (2 * n - 2)
    # 왼쪽, 오른쪽 방향으로 움직이는 경우
    # 2m - 2번 움직이면 다시 제자리로 돌아오게 되므로
    # 움직여야 할 거리를 2m - 2로 나눴을 때의 나머지 만큼만
    # 움직이게 하면 최적화가 가능합니다.
    else:
        s %= (2 * m - 2)

    # tuple에 넣을 때
    # 곰팡이 크기 정보를 먼저 넣어, 후에 곰팡이끼리 충돌이 일어날 경우
    # 크기부터 비교하여 최대인 곰팡이를 쉽게 판단할 수 있도록 합니다.
    mold[x - 1][y - 1] = (b, s, d - 1)
    
# 한 칸씩 이동하면서 곰팡이를 채취합니다.
for col in range(m):
    simulate(col)

print(ans)