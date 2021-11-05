class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:

        num_dict = dict()
        max_length = 0
        n = len(arr)
        
        for i in range(n):
            num = arr[i]
            comp = num - diff
            
            num_dict[num] = num_dict.get(comp,0) + 1
            
            # print(num,comp, "/ DICT: ", num_dict[num], num_dict.get(comp,0))
            max_length = max(max_length, num_dict[num])
        
#         SOL 2 : LIS        
#         n = len(arr)
#         length = [1]*n
        
#         for i in range(n):            
#             for j in range(i):
#                 if arr[j] + diff == arr[i]:
#                     length[i] = max(length[i], length[j]+1)
        
#         return max(length)  
        
#         SOL 1 : Counter + BFS
#         index_dict = defaultdict(list)
#         queue = deque()
#         for i, num in enumerate(arr):
#             index_dict[num].append(i)
#             queue.append((num, i, 1)) # num, index, length
#         answer = 0
        
        
#         while queue:
#             num, idx, length = queue.popleft()
#             answer = max(answer, length)
            
#             next_num = num + diff
            
#             if next_num in index_dict:
#                 for next_idx in index_dict[next_num]:
#                     if next_idx > idx:
#                         queue.append((next_num, next_idx, length+1))
        
#         return answer
        
        
        