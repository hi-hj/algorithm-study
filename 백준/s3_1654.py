import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lans = []
for i in range(n):
    lans.append(int(input()))

answer = 0
start, end = 1, max(lans)

while start <= end:
    mid = (start + end) //2
    cnt = 0
    for l in lans:
        cnt += (l//mid)
    if cnt>=k:

        start = mid +1
    else:
        end = mid -1

print(end)