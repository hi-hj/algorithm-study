class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        duplicate = 0
        pointer = 0
        if len(nums)==0:
            return 0
    
        for i in range(len(nums)):
            if nums[duplicate]!=nums[i]:
                duplicate = i
                nums[pointer+1] = nums[i]
                pointer+=1
        return pointer+1