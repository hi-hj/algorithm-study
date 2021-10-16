def ranking(number):
    if number==6:
        return 1
    elif number==5:
        return 2
    elif number==4:
        return 3
    elif number==3:
        return 4
    elif number==2:
        return 5
    else: return 6

def solution(lottos, win_nums):
    lottos = set(lottos)
    win_nums = set(win_nums)
    lottos = lottos - {0}

    fix = 6 - len(win_nums - lottos)
    var = 6 - len(lottos)

    min_num = fix
    max_num = fix + var

    return [ranking(max_num), ranking(min_num)]
    
    

# 다른 사람 풀이
# def solution(lottos, win_nums):

#     rank=[6,6,5,4,3,2,1]

#     cnt_0 = lottos.count(0)
#     ans = 0
#     for x in win_nums:
#         if x in lottos:
#             ans += 1
#     return rank[cnt_0 + ans],rank[ans]


solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])
solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])
solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])

