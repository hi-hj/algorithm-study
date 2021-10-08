import math

def lcm(x, y):
    return x*y//math.gcd(x,y)

def solution(arr):
    
    while True:
        if len(arr)==1:
            return arr[0]
        one = arr.pop()
        two = arr.pop()
        
        arr.append(lcm(one, two))