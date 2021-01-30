# https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3
# 프로그래머스 > 2019 카카오 개발자 겨울 인턴쉽
# 크레인 인형뽑기 게임 (Level 1)

def solution(board, moves):
    answer = 0
    bagooni = []
    for move in moves:
        for j in range(len(board)):
            if board[j][move-1]>0:
                bagooni.append(board[j][move-1])
                board[j][move-1]=0
                if bagooni[-1:]==bagooni[-2:-1]:
                    answer +=2
                    bagooni = bagooni[:-2]
                break
    return answer

