from collections import defaultdict
def solution(info, query):
    people = defaultdict(list)
    for i, val in enumerate(info):
        lang, end, nior, food, score = val.split()
        people[(lang, end, nior, food)].append(int(score))
    result = []

    for key in people:
        people[key].sort()
    print(people)
    for i, val in enumerate(query):
        #print(i)
        cnt = 0
        lang,_,end,_, nior,_,food,score = val.split()
        if lang =='-':lang = ('cpp', 'java', 'python')
        else:lang = [lang]
        
        if end =='-':end = ('backend','frontend')
        else:end = [end]
        
        if nior =='-':nior = ('junior', 'senior')
        else:nior = [nior]
        
        if food =='-':food = ('chicken', 'pizza')
        else:food = [food]
        
        find = []
        for l in lang:
            for e in end:
                for n in nior:
                    for f in food:
                        find.append((l,e,n,f))
        
        # 시간 복잡도 해결은 Binary Search로 탐색
        # 복잡해서 다음에...
        for quer in find:
            for man in people[quer]:
                # print(quer, man, people[quer])
                if man >=int(score):
                    cnt+=1
        result.append(cnt)
    return result



solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])



# import collections
# def solution(information, original_query):
#     info = collections.deque()
#     query = []
    
#     for informa in information:
#         lang, end, nior, food, score = informa.split()
#         info.append((int(score),lang,end,nior,food))
    
#     for quer in original_query:
#         lang2,_,end2,_, nior2,_, food2, score2 = quer.split()
#         query.append((int(score2),lang2,end2,nior2,food2))
    
#     result = [0]*len(query)
#     info = sorted(info, key = lambda x : x[0], reverse=True)
#     info = collections.deque(info)
#     print(query)
#     print(info)
#     while info:
#         man = info.popleft()
#         for i, q in enumerate(query):
#             if q[0] > man[0]:
#                 continue
#             else:
#                 break
#             # 언어 
#             if q[1] != man[1] and q[1]!='-':
#                 continue
#             # 분야
#             if q[2] != man[2] and q[2]!='-':
#                 continue
#             # 경력
#             if q[3] != man[3] and q[3]!='-':
#                 continue
#             # 소울푸드
#             if q[4] != man[4] and q[4]!='-':
#                 continue
#             result[i] +=1
#     return result