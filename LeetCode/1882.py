import heapq
from collections import deque

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:

        ready_server = []
        for i, server in enumerate(servers):
            heapq.heappush(ready_server, (server, i))
            
        run_server = []
        for i, t in enumerate(tasks):
            tasks[i] = (t,i)
        
        m = len(tasks)
        ans = [0]*m
        tasks = deque(tasks)
        queue = deque()
        time = 0
        
        while tasks or queue:
            
            # 1. 1초에 하나씩 tasks->queue에 넣기
            if tasks: queue.append(tasks.popleft())
            
            # 2. 종료된 서버 -> 반환
            while run_server:
                t, w, i = heapq.heappop(run_server)
                if t <=time:
                    heapq.heappush(ready_server, (w, i))
                else:
                    heapq.heappush(run_server, (t,w,i))
                    break
            
            # 3. 서버 돌리기
            while queue and ready_server:
                qt, qi = queue.popleft()
                w, i = heapq.heappop(ready_server)
                ans[qi] = i
                heapq.heappush(run_server, (time+qt,w,i))

            if not ready_server and time >=m:
                time = run_server[0][0]
            else:
                time+=1
        
        return ans