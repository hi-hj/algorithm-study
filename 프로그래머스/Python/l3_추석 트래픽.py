def solution(lines):
    traffic = []
    for data in lines:
        day, S, T = data.split()
        end = int(S[9:12]) + int(S[6:8])*1000 + int(S[3:5])*1000*60 + int(S[0:2])*1000*60*60
        T = int(float(T[:-1]) * 1000)
        start = end - T + 1
        traffic.append((start, end))

    traffic.sort(key = lambda x:x[1])

    max_cnt = 0

    for idx, (start, end) in enumerate(traffic):
        cnt = 0
        for s, e in traffic:
            if end<=s<end+1000 or end<=e<end+1000 or s<=end<=e:
                cnt +=1
        max_cnt = max(max_cnt, cnt)
    print(max_cnt)

    return max_cnt

        

solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"])

# solution([
# "2016-09-15 01:00:04.002 2.0s",
# "2016-09-15 01:00:07.000 2s"
# ])

# solution([
# "2016-09-15 20:59:57.421 0.351s",
# "2016-09-15 20:59:58.233 1.181s",
# "2016-09-15 20:59:58.299 0.8s",
# "2016-09-15 20:59:58.688 1.041s",
# "2016-09-15 20:59:59.591 1.412s",
# "2016-09-15 21:00:00.464 1.466s",
# "2016-09-15 21:00:00.741 1.581s",
# "2016-09-15 21:00:00.748 2.31s",
# "2016-09-15 21:00:00.966 0.381s",
# "2016-09-15 21:00:02.066 2.62s",
# ])









# def solution(lines):
#     line = []
    
#     for l in lines:
#         _,end,period = l.split()
#         h,m,s=end.split(':')
#         s,ms=s.split('.')
#         end_time = int(ms) + 1000*int(s) + 1000*60*int(m) + 1000*60*60*int(h) -75597421
#         period  = period[:-1]
#         start_time = end_time - int(float(period)*1000) +1
#         line.append((start_time, end_time))
#     line.sort(key = lambda x : x[1])
    
#     print(line)

#     cnt = -1
#     for i in range(len(line)):
#         answer = 0
#         now = line[i][1]

#         for j in range(len(line)):
#             start = line[j][0]
#             end = line[j][1]
            
#             if now<=start<now+1000 or now<=end<now+1000 or start<=now<=end:

#                 answer +=1
#         cnt = max(cnt, answer)
    
#     return cnt