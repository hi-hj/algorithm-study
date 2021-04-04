n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

max_point = 0

def back_track(cur_idx, cur_list):
    global max_point
    if cur_idx == n:
        horse = [0 for _ in range(k)]
        point = 0

        for i in range(n):
            index = cur_list[i]
            horse[index] += numbers[i]
        for h in horse:
            if h>=m-1: point +=1
        
        max_point = max(max_point, point)
        return
    
    for i in range(k):
        cur_list.append(i)
        back_track(cur_idx+1, cur_list)
        cur_list.pop()

back_track(0, [])
print(max_point)