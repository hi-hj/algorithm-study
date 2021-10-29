class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        for i in range(n,0,-1):
            for j in range(0, n+1-i):
                now = s[j:j+i]
                if now[:] == now[::-1]:
                    return now

s = 'a'
print(Solution().longestPalindrome(s))