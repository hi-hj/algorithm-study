# Two pointer
def solution(gems):
    answer = []
    shortest = len(gems)+1

    start, end = 0,0

    check_len = len(set(gems))
    contained = {}

    while end < len(gems):
        
        if gems[end] not in contained:
            contained[gems[end]] = 1
        else:
            contained[gems[end]] +=1
        end +=1
        if len(contained) == check_len:
            while start < end:
                if contained[gems[start]] > 1:
                    contained[gems[start]] -=1
                    start +=1
                elif shortest > end - start:
                    shortest = end - start
                    answer = [start+1,end]
                    break
                else:
                    break
    return answer


# import sys
# import copy
# from collections import defaultdict

# # DFS 시간 초과
# def dfs(cur_key, min_idx, max_idx):
#     global result
#     global length
#     if cur_key == len(gem_dict_keys):
#         length = min(length, max_idx - min_idx)
#         result.append((min_idx, max_idx))
#         return
#     if max_idx - min_idx > length:
#         return
    
#     for idx in gem_dict[gem_dict_keys[cur_key]]:
#         min_tmp = copy.deepcopy(min_idx)
#         max_tmp = copy.deepcopy(max_idx)
#         min_idx = min(min_idx, idx)
#         max_idx = max(max_idx, idx)
#         dfs(cur_key+1, min_idx, max_idx)
#         min_idx, max_idx = min_tmp, max_tmp


# def solution(gems):
#     global gem_dict
#     global result
#     global length
#     result = []
#     length = sys.maxsize
#     gem_dict = defaultdict(list)
    
#     for i, val in enumerate(gems):
#         gem_dict[val].append(i)

#     global gem_dict_keys
#     gem_dict_keys = list(gem_dict.keys())


#     dfs(0, sys.maxsize, -sys.maxsize)

#     result.sort(key = lambda x : (x[1]-x[0], x[0]))

#     return [result[0][0]+1,result[0][1]+1]






# Brute Force :  시간 초과
# def solution(gems):
#     length = len(set(gems))

#     for i in range(length, len(gems)+1): # 길이 순차적으로 증가
#         for j in range(0, len(gems)-i+1):
#             if length == len(set(gems[j:j+i])):
#                 return j+1, j+i

# solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
print(solution(["AA", "AB", "AC", "AA", "AC"]))
# print(solution(["XYZ", "XYZ", "XYZ"]))
# print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))