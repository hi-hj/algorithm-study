
one, two = map(int, input().strip().split(' '))
for n in range(two):
    for m in range(one):
        print('*',end='')
    if n == two-1:
        break
    print()