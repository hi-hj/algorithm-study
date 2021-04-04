import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
min_area = INT_MAX
board = [
    list(map(int, input().split()))
    for _ in range(n)
]
chess_pieces = [
    (i, j)
    for i in range(n)
    for j in range(m)
    if 1 <= board[i][j] and board[i][j] <= 5
]
print(chess_pieces)

# 말들의 방향을 표시합니다.
piece_dir = [
    [0 for _ in range(m)]
    for _ in range(n)
]

# 자신의 말로 갈 수 있는 영역을 표시합니다.
visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

# 입력으로 주어진 방향에 대해
# 말의 종류마다 북동남서 방향으로
# 이동이 가능한지 표시합니다.
can_move = [
    [],
    [1, 0, 0, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 1, 1]
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


# 움직일 수 있는 곳인지 여부를 확인합니다.
def can_go(x, y):
    return in_range(x, y) and board[x][y] != 6


# (start_x, start_y)에서 해당 타입의 말이 특정 방향을 
# 바라보고 있을 때 갈 수 있는 곳들을 전부 표시합니다.
def fill(start_x, start_y, piece_num, face_dir):
    # 북동남서 순으로 방향을 설정합니다.
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    
    for i in range(4):
        # 해당 말이 움직일 수 있는 방향인지를 확인합니다.
        # 움직일 수 없다면 pass합니다.
        if not can_move[piece_num][i]:
            continue
        
        # 갈 수 있다면, 끝날때까지 계속 진행합니다.
        # 방향은 face_dir만큼 시계방향으로 
        # 회전했을 때를 기준으로 움직입니다.
        x, y = start_x, start_y
        move_dir = (i + face_dir) % 4;
        while True:
            visited[x][y] = True
            nx, ny = x + dxs[move_dir], y + dys[move_dir]
            if can_go(nx, ny):
                x, y = nx, ny
            else:
                break


# n 개의 체스 말의 방향이 정해졌을 때 이동할 수 없는 영역의 넓이를 반환합니다.
def get_area():
    # visited 배열을 초기화합니다.
    for i in range(n):
        for j in range(m):
            visited[i][j] = 0
    
    for x, y in chess_pieces:
        # 해당 말이 정해진 방향에 있을 때 갈 수 있는 곳들을 전부 표시합니다.
        fill(x, y, board[x][y], piece_dir[x][y])
    
    area = sum([
        1
        for i in range(n)
        for j in range(m)
        if visited[i][j] == 0 and board[i][j] != 6
    ])

    return area


def search_min_area(cnt):
    global min_area
    
    # 자신의 말들의 방향이 전부 결정되었을 때, 갈 수 없는 넓이를 계산하여 갱신합니다.
    if cnt == len(chess_pieces):
        min_area = min(min_area, get_area())
        return

    # cnt 말의 방향을 설정합니다. 
    piece_x, piece_y = chess_pieces[cnt]
    
    for i in range(4):
        piece_dir[piece_x][piece_y] = i
        search_min_area(cnt + 1)


search_min_area(0)
print(min_area)