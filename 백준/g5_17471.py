import sys
from collections import deque
from itertools import combinations
n = int(input())

people = [i+1 for i in range(n)]

people_num = [0]
people_num += list(map(int, input().split()))


linked = { i:[] for i in range(1, n+1) }

for i in range(1, n+1):
    get = list(map(int, input().split()))
    linked[i] += get[1:]

def check_linked(in_list):
    queue = deque()
    visited = set()
    queue.append(in_list[0])
    visited.add(in_list[0])
    while queue:
        q = queue.popleft()
        for nq in linked[q]:
            if nq in in_list and nq not in visited:
                queue.append(nq)
                visited.add(nq)
    if visited == set(in_list):
        return True
    return False
    

answer = sys.maxsize
for i in range(1, n//2+1):
    a_list = set(combinations(people, i))
    for a in a_list:
        a = set(a)
        b = set(people) - a
        a, b= list(a), list(b)
        a_cnt = 0
        b_cnt = 0
        if check_linked(a) and check_linked(b):
            for x in a:
                a_cnt += people_num[x]
            for y in b:
                b_cnt += people_num[y]
            answer = min(answer, abs(a_cnt - b_cnt))
if answer == sys.maxsize:
    print(-1)
else:
    print(answer)

