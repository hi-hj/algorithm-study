from collections import deque

def solution(prior, location):

    output = []
    priority = deque(prior)
    numbers = deque([i for i in range(len(prior))])

    while priority:
        max_num = max(priority)

        j = priority.popleft()
        n = numbers.popleft()
        if max_num == j:
            output.append(n)
            
        else:
            priority.append(j)
            numbers.append(n)

    return output.index(location)+1




solution([2,1,3,2], 2)
solution([1,1,9,1,1,1],0)


















# import collections
# def solution(prior, location):
#     queue = collections.deque(prior)
#     idx = collections.deque([i for i in range(len(prior))])
#     result = []

#     while queue:
#         v = queue.popleft()
#         i = idx.popleft()
        
#         if not queue or max(queue) <=v:
#             result.append(i)
#         elif max(queue) > v:
#             queue.append(v)
#             idx.append(i)

#     return result.index(location)+1