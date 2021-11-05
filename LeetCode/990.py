from collections import defaultdict, deque

class Solution:
    
    def equationsPossible(self, equations: List[str]) -> bool:
        
        graph = defaultdict(list)
        
        diff = []
        for e in equations:
            if e[1:3] == "==":
                graph[e[0]].append(e[3])
                graph[e[3]].append(e[0])
            else:
                diff.append((e[0], e[3]))
        def bfs(start, check):
            visited = set()
            queue = deque()

            visited.add(start)
            queue.append(start)

            while queue:
                node = queue.popleft()
                if node ==check: return False

                for next_node in graph[node]:
                    if next_node not in visited:
                        visited.add(next_node)
                        queue.append(next_node)

            return True
    
        for start, check in diff:
            if not bfs(start, check):
                return False
        return True
        