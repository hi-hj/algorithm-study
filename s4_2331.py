# a = [1, 1, 2, 3, 4, 4]

# b= set(a)
# print(b)

import sys
input = sys.stdin.readline

a, p = map(int, input().split())

def dfs(now, a_list, circle):
    if now in circle:
        a_list = set(a_list)
        #print(a_list)
        circle = set(circle)
        #print(circle)
        print(len(a_list - circle))
        return (a_list, circle)
    else:
        if now in a_list:
            circle.append(now)
        global p
        a_list.append(now)
        now_str = str(now)
        now = 0
        for i in now_str:
            now += int(i)**p
        dfs(now, a_list, circle)

dfs(a, [], [])
#print(x)
#print(y)