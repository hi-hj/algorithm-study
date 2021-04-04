import sys
import collections
import pprint
import math
input = sys.stdin.readline

n, m, q = map(int, input().split())
circle = [collections.deque(map(int, input().split())) for _ in range(n)]

move = []
for _ in range(q):
    move.append(map(int, input().split()))

# d == 0 (시계 방향)
def move_right(num, k):
    for _ in range(k):
        a = circle[num].pop()
        circle[num].appendleft(a)


def move_left(num, k):
    for _ in range(k):
        a = circle[num].popleft()
        circle[num].append(a)


for i in range(q):
    # 1. 회전
    x, d, k = move[i]
    for i in range(n):
        if (i+1)%x ==0:
            if d == 0:
                move_right(i, k)
            elif d==1:
                move_left(i, k)

    # 2. 없앨 수 찾기
    check = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if circle[i][j] >0:
                a = circle[i][j]
                if i!=0 and circle[(i-1)][j] == a:
                    check[i][j] = True
                    check[i-1][j] = True
                
                if i!=n-1 and circle[i+1][j] == a:
                    check[i][j] = True
                    check[i+1][j] = True
                
                if circle[i][(j-1)%m] == a:
                    check[i][j] = True
                    check[i][(j-1)%m] = True
                
                if circle[i][(j+1)%m] == a:
                    check[i][j] = True
                    check[i][(j+1)%m] = True

    do_regular = True

    for i in range(n):
        for j in range(m):
            if check[i][j] == True:
                circle[i][j] = 0
                do_regular = False

    # 정규화
    if do_regular:
        calc_sum, calc_cnt = 0, 0
        for i in range(n):
            for j in range(m):
                if check[i][j] == True:
                    circle[i][j] = 0
                elif check[i][j] == False and circle[i][j]!=0:
                    calc_sum += circle[i][j]
                    calc_cnt +=1
        average = int(calc_sum /calc_cnt)

        for i in range(n):
            for j in range(m):
                if check[i][j] == False:
                    if circle[i][j] > average and circle[i][j]!=0:
                        circle[i][j]-=1
                    elif circle[i][j] < average and circle[i][j]!=0:
                        circle[i][j] +=1
            


answer = 0
for i in range(n):
    answer += sum(circle[i])
print(answer)




