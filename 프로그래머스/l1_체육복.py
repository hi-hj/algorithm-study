def solution(n, lost, reserve):
    real_lost = set(lost) - set(reserve)
    real_reserve = set(reserve) - set(lost)
    cnt = 0

    for l in real_lost:
        if l-1 in real_reserve:
            cnt +=1

            real_reserve.remove(l-1)
        elif l+1 in real_reserve:
            cnt+=1
            real_reserve.remove(l+1)

    return n - len(real_lost) + cnt


solution(5, [2,4], [1,3,5])
solution(5, [2,4], [3])
solution(3, [3], [1])


# def solution(n, lost, reserve):
#     r_lost = set(lost) - set(reserve)
#     r_reserve = set(reserve) - set(lost)
    
#     cnt = 0
#     for l in r_lost:
#         if l-1 in r_reserve:
#             r_reserve.remove(l-1)
#             cnt+=1
#         elif l+1 in r_reserve:
#             r_reserve.remove(l+1)
#             cnt+=1
#     # print(n, r_lost, r_reserve, cnt)
#     # print(len(r_lost))
#     return n - len(r_lost) + cnt
#     # for r in r_reserve:
#     #     if r-1 in r_lost:
#     #         r_lost.remove(r-1)
#     #     elif r+1 in r_lost:
#     #         r_lost.remove(r+1)