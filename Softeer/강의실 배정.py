import sys

n = int(input())

classes = []
for _ in range(n):
    start, end = map(int, input().split())
    classes.append((start, end))


classes.sort(key = lambda x: (x[1], x[0]))
answer = 0
now = 0

for start, end in classes:
    if now <= start:
        answer+=1
        now = end
    
print(answer)