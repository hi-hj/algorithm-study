def solution(n):
    F = [1, 1]
    n-=1
    
    for i in range(n-1):
        one = F[-1]
        two = F[-2]
        
        F.append(one+two)
    
    return F[n]%1234567