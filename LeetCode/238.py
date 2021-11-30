class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = [1]*n, [1]*n
        answer = [0] *n
        
        # LEFT
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
        # RIGHT
        for i in range(n-1,0,-1):
            right[i-1] = right[i] * nums[i]
        
        for i in range(n):
            answer[i] = left[i]*right[i]

        return answer
