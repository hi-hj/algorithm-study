# https://programmers.co.kr/learn/courses/30/lessons/42586
# 프로그래머스 > 스택/큐
# 기능개발 (Level 2)

# import math

# def solution(p, s):
#     answer= []
#     time = 0
#     cnt = 0
    
#     while p:
#         if (p[0]+time*s[0]) >=100:
#             p.pop(0)
#             s.pop(0)
#             cnt +=1
#         else:
#             if cnt > 0:
#                 answer.append(cnt)
#                 cnt =0
#             time +=1
#     answer.append(cnt)
#     return answer

def solution(p, s):
    answer = []
    time = 0
    now = 0

    while now < len(p):
        cnt = 0
        # 속도 더하기
        for i in range(now, len(p)):
            p[i] += s[i]
        
        for i in range(now, len(p)):
            if p[now] >=100:
                cnt +=1
                now = i+1
        
        if cnt!=0:
            answer.append(cnt)

        time +=1
        
            
    print(answer)   
    return answer


solution([93, 30, 55], 	[1, 30, 5])
solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])