n = int(input())

def define_decimal(num):
    num = int(num)
    for i in range(2, int(num**(1/2))+1):
        if num%i ==0:
            return False
    return True
start = [2,3,5,7]
candidate = []

def make_num(n,now):
    print(n,now)

    if n == 0:
        for s in start:
            return str(s) + now
    
    else:
        for i in range(1, 10):
            return make_num(n-1,now) + str(i)


print(make_num(2,''))