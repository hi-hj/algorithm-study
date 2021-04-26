import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

trees.sort(reverse=True)

start, end = 0, max(trees)
max_height = 0

while start <= end:
    mid = (start + end)//2
    cnt = 0

    for tree in trees:
        if mid >= tree or cnt>=m:
            break
        cnt += (tree-mid)
    
    if cnt >=m:
        max_height = max(max_height, mid)
        start = mid +1
    else:
        end = mid -1

print(max_height)
