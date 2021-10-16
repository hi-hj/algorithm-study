def soluion(skill, skill_tree):
    answer = 0
    for st in skill_tree:
        skillst = ''
        for s in st:
            if s in skill:
                skillst += s
        if skillst ==skill[:len(skillst)]:
            answer +=1
    return answer

# import copy
# def solution(skill, skill_trees):
#     cnt = 0 
#     skill = list(skill)
#     print(skill)

#     for st in skill_trees:
#         imsi = copy.deepcopy(skill)
#         check = True
#         for s in st:
#             if s in imsi and s!=imsi[0]:
#                 check = False
#                 break
#             if s in imsi and s==imsi[0]:
#                 imsi.pop(0)
#         if check:
#             cnt+=1
#     print(cnt)


solution('CBD', ["BACDE", "CBADF", "AECB", "BDA"])