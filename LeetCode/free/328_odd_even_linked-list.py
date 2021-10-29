# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def oddEvenList(self, head:ListNode) ->ListNode:
        print(head)
        if head is None:
            return None
        odd = head
        even = head.next
        even_head = head.next
        
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
        
        odd.next = even_head
        return head

if __name__=="__main__":
    solution = Solution()
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,None)))))
    ret = solution.oddEvenList(head)

    now = ret
    while now is not None:
        print(now.val, end = " ")
        now = now.next