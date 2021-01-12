# isalnum() : 영문자, 숫자 판별

class Solution(object):
    def isPalindrome(self, s):
        
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        while len(strs)>1:
            if strs.pop(0) != strs.pop():
                return False
        return True

# Python 3
## Type 명시
## deque 활용, pop(0) X -> popleft()
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs: Deque = collections.deque()
        
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
            
        while len(strs)>1:
            if strs.popleft() != strs.pop():
                return False
        
        return True


# Regular Expression 활용
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        
        # 정규식
        s = re.sub('[^a-z0-9]', '', s)
        
        return s == s[: : -1]