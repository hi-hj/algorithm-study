from collections import Counter

def solution(N, stages):
    n = len(stages)
    stages = Counter(stages)
    result = []
    
    for idx in range(1, N+1):
        if n <= 0: failure = 0
        else: failure = stages[idx] / n
        n -= stages[idx]
        result.append((idx, failure))

    result.sort(key = lambda x:(-x[1], x[0]))
    answer = []
    for idx, fail in result:
        answer.append(idx)
    return answer


solution(5, [2, 1, 2, 6, 2, 4, 3, 3])

















# from collections import Counter
# def solution(N, stages):
#     numbers = len(stages)
#     failure = []
#     answer = []
#     stages = Counter(stages)

#     for i in range(1, N+1):
#         fail = stages[i]

#         if numbers ==0:
#             failure.append((i, 0))
#         else:
#             failure.append((i, fail/numbers))
#         numbers -= fail
    

#     failure.sort(key = lambda x : (-x[1], x[0]))
#     print(failure)
    
#     for idx, fail in failure:
#         answer.append(idx)
#     print(answer)


# solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
# solution(4, [4,4,4,4,4])