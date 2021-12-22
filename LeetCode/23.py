
from typing import List, Optional
from collections import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for l in lists:
            while l:
                heapq.heappush(heap, l.val)
                l = l.next
        
        head = point = ListNode()
        
        
        while heap:
            val = heapq.heappop(heap)
            point.next = ListNode(val)
            point = point.next

        return head.next