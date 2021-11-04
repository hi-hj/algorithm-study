"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from collections import deque
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        emap = {e.id : e for e in employees}
        to_go = deque()
        to_go.append(id)
        total = 0
        
        while to_go:
            id = to_go.popleft()
            total+= emap[id].importance
            
            for sub_node in emap[id].subordinates:
                to_go.append(sub_node)
        
        return total

        # emap = {e.id: e for e in employees}
        # def dfs(eid):
        #     employee = emap[eid]


        #     return (employee.importance +
        #             sum(dfs(eid) for eid in employee.subordinates))
        
        # return dfs(query_id)