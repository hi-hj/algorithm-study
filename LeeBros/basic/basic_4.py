char = input()
target = input()

if target in char:
    print(char.index(target))
else:
    print(-1)