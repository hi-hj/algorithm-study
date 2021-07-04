def solution(n, k, command):
    table = [i for i in range(n)]
    deleted = []
    now = k

    for cmd in command:
        cmd = cmd.split()

        if cmd[0] =='U':
            now -= int(cmd[1])
        
        elif cmd[0] =='D':
            now += int(cmd[1])
        
        elif cmd[0] =='C':
            deleted.append(table[now])
            table.pop(now)
            if now == len(table):
                now -=1
        
        elif cmd[0] =='Z':
            now = table[now]
            back = deleted.pop()
            table.append(back)
            table.sort() # 여기서 시간 초과 발생 예상.
            now = table.index(now)

    delete = {i for i in range(n)} - set(table)
    ori_table = ['O']*n
    for idx in delete:
        ori_table[idx] = 'X'
    return ''.join(ori_table)









# import copy

# def solution(n, k, command):
#     table = [i for i in range(n)]
#     deleted = []
#     now = k

#     for cmd in command:
#         cmd = cmd.split()

#         if cmd[0] =='U':
#             now -= int(cmd[1])
        
#         elif cmd[0] =='D':
#             now += int(cmd[1])
        
#         elif cmd[0] =='C':
#             memory = copy.deepcopy(table)
#             deleted.append(memory)
#             table.pop(now)
#             if now == len(table):
#                 now -=1
        
#         elif cmd[0] =='Z':
#             now = table[now] # index --> val 값을 기억
#             back = deleted.pop()
#             table = back # 복구
#             now = table.index(now)

#     delete = set([i for i in range(n)]) - set(table)
#     ori_table = ['O']*n
#     for idx in delete:
#         ori_table[idx] = 'X'

#     return ''.join(ori_table)

solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])