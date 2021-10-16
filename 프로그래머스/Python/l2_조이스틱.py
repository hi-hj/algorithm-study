def solution(name):
    target = [min(ord(n)-ord('A'), ord('Z') - ord(n)+1) for n in name]
    length = len(name)

    cnt = 0
    i = 0

    while True:
        # 1. move
        if target[i]!=0:
            cnt += target[i]
            target[i] = 0
        if sum(target) == 0:
            break

        # 2. left or right
        left_cnt = 0
        right_cnt = 0
        
        for l in range(length):
            if target[(i-l)%length]==0:
                left_cnt +=1
            else:
                break
        for r in range(length):
            if target[(i+r)%length]==0:
                right_cnt +=1
            else:
                break
        
        if left_cnt < right_cnt:
            cnt += left_cnt
            i = (i-left_cnt)%length
        else:
            cnt += right_cnt
            i = (i+right_cnt)%length

    return cnt


solution('JEROEN')
solution('JAN')
# def solution(name):
#     target = [min(ord(n)-ord('A'), ord('Z')-ord(n)+1)  for n in name]
#     length = len(name)
    
#     cnt = 0
#     i = 0
#     while True:
#         #1. move
#         if target[i]!=0:
#             cnt += target[i]
#             target[i] = 0
#         if sum(target)==0:
#             break

#         #2. < or >
#         left_cnt, right_cnt = 0,0
#         for l in range(length):
#             if target[(i-l)%length]==0:
#                 left_cnt +=1
#             else:
#                 break
#         for r in range(length):
#             if target[(i+r)%length]==0:
#                 right_cnt+=1
#             else:
#                 break
        
#         if left_cnt < right_cnt:
#             i = (i-left_cnt)%length
#             cnt+=left_cnt
#         else:
#             i = (i+right_cnt)%length
#             cnt+=right_cnt


            
#     return cnt