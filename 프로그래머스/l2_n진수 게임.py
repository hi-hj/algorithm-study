def conv(number,base):
    T = '0123456789ABCDEF'
    i, j = divmod(number,base)
    if i ==0:
        return T[j]
    else:
        return conv(i, base) + T[j]

def solution(n,t,m,p):
    nums = ''
    num = 0
    now = p-1
    result = ''
    
    while t>0:
        if len(nums) > now: # 있는 경우
            result += nums[now]
            now += m
            t-=1
        else: # 없는 경우 : 추가
            nums += conv(num,n)
            num+=1
    
    return result





solution(2,4,2,1)
solution(16,16,2,1)
solution(16,16,2,2)