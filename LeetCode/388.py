class Solution:
    def lengthLongestPath(self, input: str) -> int:
        paths = input.split('\n')
        stack = []
        answer = 0

        for path in paths:
            # 1. Preprocess
            cnt = path.count('\t')
            for i in range(cnt):path = path.replace('\t','')

            # 2. File Length
            if '.' in path:
                directory = None
                while stack and stack[-1][0] >=cnt: directory = stack.pop()
                
                sentence = ''
                for _, string in stack:
                    sentence += string
                    sentence += '/'
                sentence += path
                answer = max(answer, len(sentence))
                
                if directory is not None:
                    stack.append(directory)
                continue
            
            
            # 3. Add/Remove Stack
            if not stack: stack.append((cnt, path))
            elif stack[-1][0] < cnt: stack.append((cnt, path))
            else:
                while stack and stack[-1][0] >= cnt:
                    stack.pop()
                stack.append((cnt, path))
        
        return answer


# class Solution:
#     def lengthLongestPath(self, input: str) -> int:
#         mx, cur_len = 0, 0
#         input = input.split("\n")
#         stack = []
#         for p in input:
#             p = p.split("\t")
# 			# len(p) = p's corresponding layer
# 			# we pop the stack until we reach p's parent directory
#             while len(stack) >= len(p):
#                 cur_len -= len(stack.pop())
            
#             stack.append(p[-1])
#             cur_len += len(p[-1])
            
#             if len(p[-1].split(".")) > 1:
#                 mx = max(mx, len(stack) + cur_len - 1)

#         return mx

    

Solution().lengthLongestPath("dir\n        file.txt")
# Solution().lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")