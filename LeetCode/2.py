from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 1. Optimization way 
        head = point = ListNode()
        extra = 0
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            new_val = l1_val + l2_val + extra
            if new_val > 9:
                new_val -= 10
                extra = 1
            else:
                extra = 0
            point.next = ListNode(new_val)
            point = point.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if extra == 1:
            point.next = ListNode(1)
        
        return head.next


        l1_str, l2_str = "", ""
        
        while l1:
            l1_str += str(l1.val)
            l1 = l1.next
        while l2:
            l2_str += str(l2.val)
            l2 = l2.next
        
        result = eval(l1_str[::-1]+"+"+l2_str[::-1])
        result = list(str(result)[::-1])
        
        head = point = ListNode()

        for num in result:
            point.next = ListNode(int(num))
            point = point.next
        return head.next