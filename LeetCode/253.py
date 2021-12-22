from typing import List
from collections import deque, heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # 1. Prepare
        # Sort : key - start
        # variable : ready_room, meeting_room
        
        # 2. run
        # popleft : start, end
        # Check meeting_room -> add to ready_room
        # if ready_room is enough -> assign it
        # not room : add new room
        
        intervals.sort(key = lambda x : x[0])
        intervals = deque(intervals)
        
        meeting_room = []
        ready_room   = 0
        count        = 0
        
        while intervals:
            start, end = intervals.popleft()
            while meeting_room and meeting_room[0]<=start:
                heapq.heappop(meeting_room)
                ready_room+=1
            
            if ready_room ==0:
                ready_room+=1
                count+=1
            ready_room-=1
            heapq.heappush(meeting_room, end)
            
        return count