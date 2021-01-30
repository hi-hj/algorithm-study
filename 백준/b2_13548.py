import sys
input = sys.stdin.readline

n = int(input())
test = list(map(int, input().split()))
b, c = map(int, input().split())


cnt = 0
for i in range(n):
    test[i] -= b
    cnt +=1

    if test[i]>0:
        x, y = divmod(test[i], c)
        cnt += x
        if y>0:
            cnt +=1

print(cnt)
