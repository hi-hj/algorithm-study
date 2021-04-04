import sys
n, m ,h = map(int, input().split())

memory_leak = []
for _ in range(m):
    a, b = map(int, input().split())
    memory_leak.append((a-1, b-1))


def check_result(add_memory_leak):
    data = [[0]*n for _ in range(h+1)]
    check_answer = [0]*n
    for i in range(1,n+1):
        x,y = 0, i-1
        data[x][y] = i
        check_answer[y] = i
        visited = []
        while True:
            if ((x, y) in memory_leak or (x, y) in add_memory_leak) and (x, y) not in visited:
                visited.append((x, y))
                x, y = x, y+1
            elif ((x, y-1) in memory_leak or (x, y-1) in add_memory_leak) and (x, y-1) not in visited:
                visited.append((x, y-1))
                x, y = x, y-1
            else:
                x, y = x+1, y
                if x+1>h+1:
                    break
            data[x][y] = i
    

    if check_answer == data[h]: return True
    else: return False



candidate_memory = []
for i in range(h+1):
    for j in range(n-1):
        candidate_memory.append((i, j))
for x, y in memory_leak:
    candidate_memory.remove((x, y))
    if (x, y-1) in candidate_memory: candidate_memory.remove((x, y-1))
    if (x, y+1) in candidate_memory: candidate_memory.remove((x, y+1)) 

def check_candidate(candidate):
    for x, y in candidate:
        if (x, y-1) in candidate or (x, y+1) in candidate:
            return False
    return True

answer = sys.maxsize


def back_tracking(cur_idx, cur_list):
    global answer

    if cur_idx == len(candidate_memory) and len(cur_list)<4:
        if check_candidate(cur_list):
            if check_result(cur_list):
                answer = min(answer, len(cur_list))
        return
    if len(cur_list)>3 or len(cur_list)>answer:
        return
    back_tracking(cur_idx+1, cur_list)

    cur_list.append(candidate_memory[cur_idx])
    back_tracking(cur_idx+1, cur_list)
    cur_list.pop()

back_tracking(0, [])


if answer == sys.maxsize:
    print(-1)
else:
    print(answer)