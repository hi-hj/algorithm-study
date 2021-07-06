def solution(answers):

    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    thr = [3,3,1,1,2,2,4,4,5,5]

    answer = [0,0,0]

    for i in range(len(answers)):
        if answers[i] == one[i%5]:
            answer[0]+=1
        if answers[i] == two[i%8]:
            answer[1]+=1
        if answers[i] == thr[i%10]:
            answer[2]+=1
    
    max_score = max(answer)
    result = []
    for i, man in enumerate(answer):
        if man == max_score:
            result.append(i+1)
    print(result)
    return result


solution([1,2,3,4,5])
solution([1,3,2,4,2])



# def solution(answers):
#     one = [1,2,3,4,5]
#     two = [2,1,2,3,2,4,2,5]
#     thr = [3,3,1,1,2,2,4,4,5,5]
    
#     score = [0,0,0]
#     for i in range(len(answers)):
#         if answers[i] == one[i%5]:
#             score[0]+=1
#         if answers[i] == two[i%8]:
#             score[1]+=1
#         if answers[i] == thr[i%10]:
#             score[2]+=1
#     max_score = max(score)
#     result = []
#     for i in range(len(score)):
#         if score[i]==max_score:
#             result.append(i+1)
#     return result