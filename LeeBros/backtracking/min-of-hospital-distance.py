import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
people = []
hospital = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            people.append((i, j))
        elif grid[i][j] ==2:
            hospital.append((i, j))
answer = 9999
def calc_length(people, hospital):
    global answer
    length = 0
    for px, py in people:
        min_man_to_hospital = 99999
        for hx, hy in hospital:
            man_to_hospital = abs(px-hx) + abs(py-hy)
            min_man_to_hospital = min(min_man_to_hospital, man_to_hospital)
        length += min_man_to_hospital

    answer = min(length, answer)


def back_track(cur_idx, cur_list):
    if cur_idx == len(hospital) and len(cur_list)==m:
        # 함수 실행

        calc_length(people, cur_list)
        return
    
    elif cur_idx == len(hospital) and len(cur_list)!=m:
        # 걍 종료
        return
    
    # 이건 안 포함
    back_track(cur_idx+1, cur_list)
    # 이건 포함
    cur_list.append(hospital[cur_idx])
    back_track(cur_idx+1, cur_list)
    cur_list.pop()

    
back_track(0, [])

print(answer)