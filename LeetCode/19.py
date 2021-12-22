from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. Calc len of head
        point = head
        sz = 0
        while point:
            sz+=1
            point = point.next
        index = 0
        
        # 2. Get 'after' node
        remove_index = sz - n
        point = head
        while index < remove_index:
            point = point.next
            index+=1
        after = point.next
        
        # 3. Link 'after' node
        point = head
        index = 0
        while index < remove_index:
            if index == remove_index-1:
                point.next = after
                break
            point = point.next
            index+=1
        
        # * Edge Case
        if remove_index == 0:
            return after
        
        return head

        
            