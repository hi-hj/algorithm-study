from sys import stdin
read = stdin.readline

dic ={}

for i in range(int(read())):
    dic[i+1] = set()
for j in range(int(read())):
    a, b = map(int, read().split())
    dic[a].add(b)
    dic[b].add(a)


print(dic)
visited = []

def bfs(start, dic):
    queue = [start]
    while queue:
        for i in dic[queue.pop()]:
            if i not in visited:
                visited.append(i)
                queue.append(i)


bfs(1, dic)
print(len(visited)-1)