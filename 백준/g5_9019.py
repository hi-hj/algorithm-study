# 변수를 설정하는게 포인트
## 함수를 떠올렸다면
### 숫자가 움직이는 과정을 따라가면서, 변수를 효율적으로 설계하자..

import sys
input = sys.stdin.readline

import collections


def bfs():
    queue = collections.deque()
    queue.append([start, ""])
    while queue:
        num, result = queue.popleft()
        
        D = (num*2) % 10000
        if D == end:
            return result +"D"
        elif arr[D]==0:
            arr[D]=1
            queue.append([D, result+"D"])
        
        S = num-1
        if num==0:
            S = 9999
        if S == end:
            return result +"S"
        elif arr[S]==0:
            arr[S]=1
            queue.append([S, result+"S"])
         
        L = (num%1000*10) + (num//1000)
        if L == end:
            return result +"L"
        elif arr[L]==0:
            arr[L]=1
            queue.append([L, result+"L"])
         
        R = (num%10*1000) + (num//10)
        if R == end:
            return result +"R"
        elif arr[R]==0:
            arr[R]=1
            queue.append([R, result+"R"])


test_case = int(input())

for _ in range(test_case):
    start, end = map(int, input().split())
    arr = [0 for _ in range(10000)]
    print(bfs())