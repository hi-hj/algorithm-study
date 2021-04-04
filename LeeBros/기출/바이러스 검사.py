import sys
input = sys.stdin.readline

n = int(input())

customer = list(map(int, input().split()))
a, b = map(int, input().split())


answer = n

for i in range(n):
    customer[i] -= a

for i in range(n):
    if customer[i] >0:
        x, y = divmod(customer[i], b)
        answer += x
        if y !=0:
            answer +=1

print(answer)
