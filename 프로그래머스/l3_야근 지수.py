import heapq

def solution(n, works):
    heap = []
    for work in works:
        heap.append([-work, work])
    heapq.heapify(heap)
    
    for i in range(n):
        max_value = heapq.heappop(heap)
        if max_value[1] >0: max_value[1] -=1
        heapq.heappush(heap, [-max_value[1], max_value[1]])
    result = 0
    for _, val in heap:
        result += val**2
    return result