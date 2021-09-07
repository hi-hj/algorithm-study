from collections import defaultdict


def solution(msg):
    # Set Default
    word_dict = defaultdict(int)
    for i in range(65, 91):
        word_dict[chr(i)] = i - 64


    idx = 0
    last = 26
    result = []
    while idx < len(msg):
        now = msg[idx]
        # print(now, result, word_dict)
        
        while True:

            if idx == len(msg)-1 or now+msg[idx+1] not in word_dict:
                # print("*X:", now, idx)
                result.append(word_dict[now])
                last +=1
                if idx >= len(msg)-1:
                    break
                now += msg[idx+1]        
                word_dict[now] = last
                break
            else:
                # print("**O:", now, idx)
                now += msg[idx+1]
                idx +=1
                
        idx +=1
    return result


# solution("KAKAO")
solution("TOBEORNOTTOBEORTOBEORNOT")
solution("ABABABABABABABAB")


# import collections
# def solution(msg):
#     word_dict = collections.defaultdict(int)
#     # set dict
#     for i in range(65, 91):
#         word_dict[chr(i)] = i-64
#     result = []
    
#     max_idx = 27
    
#     i = 0
#     while i < len(msg):
#     # for i in range(len(msg)):
#         now_str = msg[i]
        
#         for j in range(i+1, len(msg)):
#             now_str = now_str + msg[j]
#             i+=1
#             # 사전 추가
#             if now_str not in word_dict:
#                 word_dict[now_str] = max_idx
#                 max_idx +=1
#                 i-=1
#                 break
#         #출력
#         if i != len(msg)-1:
#             now_str = now_str[:-1]
#         result.append(word_dict[now_str])
#         i+=1

#     return result