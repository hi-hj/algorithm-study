# https://programmers.co.kr/learn/courses/30/lessons/42586
# 프로그래머스 > 스택/큐
# 기능개발 (Level 2)

import math

def solution(p, s):
    answer= []
    time = 0
    cnt = 0
    while p:
        if (p[0]+time*s[0]) >=100:
            p.pop(0)
            s.pop(0)
            cnt +=1
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt =0
            time +=1
    answer.append(cnt)
    return answer