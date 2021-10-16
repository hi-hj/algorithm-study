from itertools import permutations
def solution(n, k):
    people = [i for i in range(1, n+1)]
    new = list(permutations(people, n))
    return new[k-1]

# import copy
# def solution(n, k):
#     people = [i for i in range(1, n+1)]
#     result = []
#     def dfs(cur_idx, cur_list):
#         if cur_idx == n:
#             new = copy.deepcopy(cur_list)
#             result.append(new)
#             return
#         if len(result) >= k:
#             return
#         for p in people:
#             if p not in cur_list:
#                 cur_list.append(p)
#                 dfs(cur_idx+1, cur_list)
#                 cur_list.pop()
#     dfs(0,[])
    
#     return result[k-1]