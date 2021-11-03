from collections import deque
import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        answer = []
        heap = []
        for idx, (enque, process) in enumerate(tasks):
            tasks[idx] = (enque, process, idx)
        tasks.sort()
        tasks = deque(tasks)
        time = 0

        while tasks:
            # ADD TASK
            while tasks and tasks[0][0] <=time:
                e, p, i = tasks.popleft()
                heapq.heappush(heap, (p, i))
            if heap:
                p, i = heapq.heappop(heap)
                time +=p
                answer.append(i)
            else:
                time = tasks[0][0]
                
        while heap:
            p, i = heapq.heappop(heap)
            answer.append(i)
        return answer
