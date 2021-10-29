import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Better Solution
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]
        
        # My Solution
        
        # s_list = []
        # s = s.lower()
        # for string in s:
        #     if string.isalpha() or string.isdigit():
        #         s_list.append(string)
        # n = len(s_list)
        
        # for i in range(n//2):
        #     if s_list[i] != s_list[n-1-i]:
        #         return False
        # return True


s = "0p"
print(Solution().isPalindrome(s))
