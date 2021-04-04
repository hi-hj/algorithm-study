import sys
input = sys.stdin.readline
import collections


test_case = int(input())

for _ in range(test_case):
    n, m = map(int, input().split())
    bead_list = []
    bead_vector = collections.deque()
    for _ in range(m):
        x, y, v = input().split()
        bead_list.append((int(x)-1, int(y)-1))
        bead_vector.append(v)

    test = [[0]*n for _ in range(n)]
    for x, y in bead_list:
        test[x][y] = 1

    for _ in range(2500):
        for i in range(len(bead_list)):
            x, y = bead_list.pop(0)
            v = bead_vector.popleft()


            if v =='L':
                if y==0: 
                    bead_vector.append('R')
                    bead_list.append((x, y))
                else:
                    test[x][y] -=1
                    test[x][y-1] +=1
                    bead_vector.append('L')
                    bead_list.append((x, y-1))
                    
            elif v =='R':
                if y+1>=n: 
                    bead_vector.append('L')
                    bead_list.append((x, y))
                else:
                    test[x][y] -=1
                    test[x][y+1] +=1
                    bead_vector.append('R')
                    bead_list.append((x, y+1))

            elif v =='U':
                if x==0:
                    bead_vector.append('D')
                    bead_list.append((x, y))
                else:
                    test[x][y] -=1
                    test[x-1][y] +=1
                    bead_vector.append('U')
                    bead_list.append((x-1, y))
            
            elif v =='D':
                if x+1>=n:
                    bead_vector.append('U')
                    bead_list.append((x, y))
                else:
                    test[x][y] -=1
                    test[x+1][y] +=1
                    bead_vector.append('D')
                    bead_list.append((x+1, y))
    
        for i in range(n):
            for j in range(n):
                if test[i][j]>=2:
                    #print(test, bead_list)
                    for k in range(test[i][j]):
                        bead_list.remove((i, j))
                    test[i][j] = 0

        # bead_list = set(bead_list)
    #print(bead_list)
    #print(len(bead_list))
    result = 0
    for i in range(n):
        result += sum(test[i])
    print(result)
