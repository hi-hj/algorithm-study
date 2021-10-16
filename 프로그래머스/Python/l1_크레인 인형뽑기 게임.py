import pprint

def solution(board, moves):

    bascket = []
    n = len(board)
    answer = 0
    for move in moves:
        
        for i in range(n):
            if board[i][move-1] !=0:
                item = board[i][move-1]
                board[i][move-1] = 0

                if bascket and bascket[-1] == item:
                    bascket.pop()
                    answer +=2
                    break
                bascket.append(item)
                break
    
    return answer




solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])









# https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3
# 프로그래머스 > 2019 카카오 개발자 겨울 인턴쉽
# 크레인 인형뽑기 게임 (Level 1)
# import pprint
# def solution(board, moves):
#     answer = 0
#     bomb_list = []
#     n = len(board)

#     for m in moves:
#         for i in range(n):
#             if board[i][m-1]!=0:
#                 bomb_list.append(board[i][m-1])
#                 if len(bomb_list)>=2 and bomb_list[-1] == bomb_list[-2]:
#                     answer+=2
#                     bomb_list.pop()
#                     bomb_list.pop()
#                 board[i][m-1] = 0
#                 break

#     return answer



# board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
# moves = [1,5,3,5,1,2,1,4]
# solution(board, moves)






















# def solution(board, moves):
#     answer = 0
#     bagooni = []
#     for move in moves:
#         for j in range(len(board)):
#             if board[j][move-1]>0:
#                 bagooni.append(board[j][move-1])
#                 board[j][move-1]=0
#                 if bagooni[-1:]==bagooni[-2:-1]:
#                     answer +=2
#                     bagooni = bagooni[:-2]
#                 break
#     return answer

