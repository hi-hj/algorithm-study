import copy
def can_go(ban_id, user_id):
    if len(ban_id) != len(user_id):
        return False
    for i in range(len(ban_id)):
        if ban_id[i] == '*':
            continue
        elif ban_id[i]!=user_id[i]:
            return False
    return True
            

def solution(user_id, banned_id):

    global result
    result = set()
    
    def dfs(cur_idx, cur_list):
        if cur_idx == len(banned_id):
            copy_list = copy.deepcopy(cur_list)
            copy_list.sort()
            copy_list = tuple(cur_list)
            result.add(copy_list)
            return
        for user in user_id:
            if can_go(banned_id[cur_idx], user) and user not in cur_list:
                cur_list.append(user)
                dfs(cur_idx+1, cur_list)
                cur_list.pop()
    
    dfs(0, [])

    return len(result)

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
solution(user_id, banned_id)



# import copy
# def can_go(ban_id, user_id):
#     if len(ban_id) != len(user_id):
#         return False
#     for i in range(len(ban_id)):
#         if ban_id[i] == '*':
#             continue
#         elif ban_id[i]!=user_id[i]:
#             return False
#     return True
            

# def solution(user_id, banned_id):
#     global cnt
#     global result
#     cnt = 0
#     result = []
    
#     def dfs(cur_idx, cur_list):
#         global cnt
#         if cur_idx == len(banned_id):
#             print(cur_list)
#             cnt +=1
#             copy_list = copy.deepcopy(cur_list)
#             result.append(copy_list)
#             return
#         for user in user_id:
#             if can_go(banned_id[cur_idx], user) and user not in cur_list:
#                 cur_list.append(user)
#                 dfs(cur_idx+1, cur_list)
#                 cur_list.pop()
    
#     dfs(0, [])
#     print(cnt)
#     print(result)
    
#     for i in range(cnt):
#         result[i].sort()
#         result[i] = set(result)
#     print(result)
#     result = set(result)
#     print(result)
# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id = ["fr*d*", "*rodo", "******", "******"]
# solution(user_id, banned_id)