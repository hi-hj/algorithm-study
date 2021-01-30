import sys
input = sys.stdin.readline

start, end = map(int, input().split())

decimal = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
for i in range(len(decimal)):
    decimal[i] = decimal[i]**2

cnt = 0
for i in range(start, end+1):
    if i in decimal:
        cnt+=1
print(cnt)