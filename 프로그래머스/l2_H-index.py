def solution(citations):
    answer = 0

    citations.sort(reverse=True)
    h = len(citations)
    now = 0
    while True:
        cnt = now

        for i in range(now, len(citations)):
            if citations[i] >=h:
                cnt+=1
            else:
                now = i-1
                break
        if cnt >=h:
            return h
        h-=1
    
    return answer


solution([3,0,6,1,5])









# def solution(citations):
#     citations.sort(reverse=True)
#     h = len(citations)
#     now = 0
    
#     while True:
#         cnt = now
#         for i in range(now, len(citations)):
#             if citations[i]>=h: cnt +=1
#             else:
#                 now = i-1
#                 break
#         if cnt >=h: return h
#         h -=1