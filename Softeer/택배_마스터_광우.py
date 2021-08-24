import sys
from itertools import permutations

n, m, k = map(int, input().split())
rails = list(map(int, input().split()))

can_make = list(permutations(rails, len(rails)))

def calc_weight(rail):
    weight = 0
    now_index = 0

    for i in range(k):
        now_weight = 0
        while now_weight+rail[now_index]<=m:
            now_weight += rail[now_index]
            now_index +=1
            if now_index == len(rail):
                now_index = 0
        weight += now_weight
            
    return weight
answer = sys.maxsize
for rail in can_make:
    answer = min(answer, calc_weight(rail))
print(answer)
