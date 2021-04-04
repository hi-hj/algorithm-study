import sys
input = sys.stdin.readline

n, l = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


def can_go(board):
    length = len(board)
    slide = [False]*length
    now, cnt = board[0], 1
    for i in range(1, length):
        if board[i] == now:
            cnt += 1
        elif board[i] != now:
            if abs(board[i]-now)>1: return False
            
            elif board[i]==now+1:
                if l > cnt: return False
                else:
                    for c in range(1, l+1):
                        if slide[i-c] == True: return False
                        else:
                            slide[i-c] = True                
            now = board[i]
            cnt = 1
    board.reverse()
    slide.reverse()

    now, cnt = board[0], 1
    for i in range(1, length):
        if board[i] == now:
            cnt += 1
        elif board[i] != now:
            if abs(board[i]-now)>1: return False
            
            elif board[i]==now+1:
                if l > cnt: return False
                else:
                    for c in range(1, l+1):
                        if slide[i-c] == True: return False
                        else:
                            slide[i-c] = True                
            now = board[i]

    return True



answer = 0               
for i in range(n):
    board = [0]*n
    for j in range(n):
        board[j] = grid[i][j]
    if can_go(board):

        answer+=1

for i in range(n):
    board = [0]*n
    for j in range(n):
        board[j] = grid[j][i]
    if can_go(board):

        answer+=1


print(answer)
        
