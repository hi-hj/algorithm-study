def solution(dartResult):
    print(dartResult)


solution("1D#2S*3S")


# def solution(dartResult):
#     answer = []
#     dartResult = dartResult.replace('10','k')
#     point = ['10' if i == 'k' else i for i in dartResult]
#     print(point)

    
#     i = -1
#     sdx = ['S','D','T']
#     for j in range(len(point)):
#         if point[j] == 'S':
#             answer[i] = answer[i]**1
#         elif point[j] == 'D':
#             answer[i] = answer[i]**2
#         elif point[j] =='T':
#             answer[i] = answer[i]**3
        
#         elif point[j] == '*':
#             answer[i] *=2
#             if i!=0:
#                 answer[i-1] *=2
#         elif point[j] == '#':
#             answer[i] = -answer[i]

#         else:
#             answer.append(int(point[j]))
#             i +=1
#     return sum(answer)