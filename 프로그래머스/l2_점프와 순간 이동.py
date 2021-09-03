def solution(n):
    print(n)
    cnt = 0

    while n > 0 :
        n,q = divmod(n,2)
        print(n,q)
        if q == 1:
            cnt +=1
        print('AFTER', n,q)
    print(cnt)
        

solution(5000)