n = int(input())
numbers = list(map(int, input().split()))


sort_numbers = sorted(numbers)

# print(numbers)
# print(sort_numbers)

for i in range(n):
    find = numbers[i]
    get = sort_numbers.index(find)
    sort_numbers[get] = -1
    print(get+1, end=' ')