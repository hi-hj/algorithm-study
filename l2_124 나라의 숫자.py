# https://programmers.co.kr/learn/courses/30/lessons/12899
# 프로그래머스 > 연스문제
# 124 나라의 숫자 (Level 2)

def solution(n):
    if n<=3:
        return '124'[n-1]
    else:
        q, r= divmod(n-1,3)
        return solution(q) + '124'[r]
