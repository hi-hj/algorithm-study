import heapq

def solution(operations):
    heap = []

    for operation in operations:
        o, n = operation.split()

        if o =='I':
            heapq.heappush(heap, int(n))

        elif o =='D' and heap:
            if n =='1':
                heap.remove(max(heap))
                heapq.heapify(heap)
            elif n=='-1':
                heapq.heappop(heap)
    print(heap)

    if not heap:
        return [0,0]
    else:
        return [max(heap), min(heap)]


solution(["I 16","D 1"])

solution(["I 7","I 5","I -5","D -1"])











# import heapq

# def solution(oper):
#     queue = []
#     for op in oper:
#         o, n = op.split()
        
#         if o == 'I':
#             heapq.heappush(queue, int(n))
#         elif o =='D' and queue:
#             if n=='1':
#                 queue.remove(max(queue))
#                 heapq.heapify(queue)
#             elif n=='-1':
#                 a= heapq.heappop(queue)
#     if not queue:
#         return [0,0]
#     else:
#         return [max(queue), min(queue)]