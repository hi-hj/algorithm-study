import sys
input = sys.stdin.readline

n = int(input())


numbers = list(map(int, input().split()))


keep = True
index = numbers.index(max(numbers))

while keep:
    index = numbers.index(max(numbers))
    if index == 0:
        keep = False
    numbers = numbers[:index]
    print(index+1, end=' ')
    