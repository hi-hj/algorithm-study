import heapq

def solution(scoville, k):

    heapq.heapify(scoville)
    cnt = 0

    while len(scoville)>1:
        first = heapq.heappop(scoville)

        if first >= k:
            heapq.heappush(scoville, first)
            break
        
        second = heapq.heappop(scoville)

        new = first + second*2
        heapq.heappush(scoville, new)
        cnt+=1
    
    check = heapq.heappop(scoville)
    if check < k:
        return -1
    return cnt


solution([1, 2, 3, 9, 10, 12], 7)











# import heapq

# def solution(scoville, k):
#     heapq.heapify(scoville)
#     cnt = 0
#     while len(scoville) >1:
#         first = heapq.heappop(scoville)
#         if first >= k:
#             heapq.heappush(scoville, first)
#             heapq.heappush
#             break
#         second = heapq.heappop(scoville)
#         heapq.heappush(scoville, first + 2*second)
#         cnt +=1
    
#     check = heapq.heappop(scoville)
#     if check < k:
#         return -1
#     return cnt