from bisect import bisect_left
from collections import deque

def solution(n, t, m, timetable):
    times= []
    for time in timetable:
        times.append(int(time[0:2])*60 + int(time[3:]))
    times.sort()

    start_time = 540 # 09:00
    last_time = 540 + t*(n-1)
    idx = bisect_left(times, last_time+1)
    times = times[:idx]

    times = deque(times[:n*m])
    

    check = {}

    for bus_time in range(start_time, last_time+t, t):
        check[bus_time] = []
        for _ in range(m):
            if times and times[0]<=bus_time:
                man = times.popleft()
                check[bus_time].append(man)

    
    if check[last_time] and len(check[last_time])==m:
        last = check[last_time].pop()
        h, m = divmod(last-1, 60)
        return str(h).zfill(2)+":"+str(m).zfill(2)

    else:
        h, m = divmod(last_time, 60)
        return str(h).zfill(2)+":"+str(m).zfill(2)





solution(1,1,5,["08:00", "08:01", "08:02", "08:03"])
solution(2,10,2,["09:10", "09:09", "08:00"])
solution(2,1,2,["09:00", "09:00", "09:00", "09:00"])
solution(1,1,5,["00:01", "00:01", "00:01", "00:01", "00:01"])
solution(1,1,1,["23:59"])
solution(10, 60, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"])





# import collections
# import sys

# def time_to_str(time):
#     hour = time // 60
#     minute = time % 60
#     hourStr = str(hour)
#     minuteStr = str(minute)
#     if hour < 10:
#         hourStr = "0"+ hourStr
#     if minute < 10:
#         minuteStr = "0" + minuteStr
    
#     return hourStr+":"+minuteStr

# def solution(n, t, m, timetable):
#     time_table = collections.deque()
#     for time in timetable:
#         h, mm = time.split(':')
#         time_table.append(int(h)*60 + int(mm)-540)
#     time_table = sorted(time_table)
#     time_table = collections.deque(time_table)
    
#     bus = [i for i in range(n)]
#     for i in range(n):
#         bus[i] *= int(t)

#     last = sys.maxsize
#     for b in bus:
#         cnt = 0
#         while True:
#             if cnt == m:
#                 break
#             if time_table[0] <= b:
#                 cnt +=1
#                 last = time_table.popleft()
#             else:
#                 break
#             if not time_table:
#                 break
    
#     print(time_table)
#     print(b, last, cnt)
    
#     b += 540
#     last += 540

    
#     if cnt < m:

#         return time_to_str(b)
#     else:
#         return time_to_str(last-1)