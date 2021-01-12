class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        q: List = []
        #q: Deque = collections.deque()
        # q.pop() --> q.popleft() 더 효율적 ! 
        while head is not None:
            q.append(head.val)
            head = head.next
        #print(q)
        
        while len(q)>1:
            if q.pop() != q.pop(0):
                return False
        
        return True



class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        rev = None
        slow = fast =head
        
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
            
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev