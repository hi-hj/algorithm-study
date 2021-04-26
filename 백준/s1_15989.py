T = int(input())
for _ in range(T):
    n = int(input())
    print('*****')
    can_make = [0, 1, 2, 3, 4]

    for i in range(5, n+1):
        cnt = 0
        cnt += can_make[i//2] + can_make[i- i//2]
        # for x in range(1, i//2+1):
        #     print(x, i-x)
        #     cnt += (can_make[x] + can_make[i-x])
            # for y in range(i-1, (i+1)//2, -1):
            #     print(x,y)
            #     cnt += (can_make[x] + can_make[y])
        can_make.append(cnt)
    
    print(can_make[n])

    print('#####')
    print(can_make)
