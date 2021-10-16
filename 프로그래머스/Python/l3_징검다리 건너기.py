import sys

def solution(stones, k):
    answer = 0
    start, end = 0, sys.maxsize

    while start <= end:
        people = (start + end) // 2
        jump = 0

        for stone in stones:
            if stone - people < 0:
                jump +=1
            else:
                jump = 0
            
            if jump >=k:
                break
        
        if jump < k :
            answer = max(answer, people)
            start = people + 1
        else:
            end = people -1 
    return answer
















# import sys
# def solution(stones, k):
#     answer = 0
#     start, end = 0, sys.maxsize
    
#     while start <= end:
#         mid = (start + end)//2
#         jump = 0

#         for stone in stones:
#             if stone - mid < 0: # 연속 jump인 경우만 +
#                 jump +=1
#             else: # 중간에 끊기면 리셋
#                 jump = 0
            
#             # jump한 수가 k개 이상이면 중단
#             if jump >= k:
#                 break
        
#         if jump < k:
#             answer = max(answer, mid)
#             start = mid + 1
#         else:
#             end = mid -1
    
#     return answer
        

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
solution(stones, k)