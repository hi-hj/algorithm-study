import collections

n = int(input())


def operations(n, calc):
    if calc == 0:
        return n-1
    elif calc == 1:
        return n+1
    elif calc == 2 and n%2 ==0:
        return n/2
    elif calc ==3 and n%3 ==0:
        return n/3


queue = collections.deque()

queue.append((n, 0))

visited = [n]

while queue:
    n, cnt = queue.popleft()
    if n == 1:
        print(cnt)
        break

    for i in range(4):
        new_n = operations(n, i)
        if new_n and new_n not in visited:
            queue.append((new_n, cnt+1))
            visited.append(new_n)
