import sys
input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

result = []

arr1.sort()

for num in arr2:
    start = 0
    end = len(arr1)-1
    find = False

    while start <= end:
        mid = (start + end) //2
        
        if num == arr1[mid]:
            find = True
            break
        
        if num > arr1[mid]:
            start = mid +1
        else:
            end = mid -1
    if find:
        result.append(1)
    else:
        result.append(0)

for i in result:
    print(i)

    