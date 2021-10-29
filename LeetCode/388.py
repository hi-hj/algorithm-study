class Solution:
    def lengthLongestPath(self, input: str) -> int:
        paths = input.split('\n')
        stack = []
        answer = 0

        for path in paths:
            # 1. Preprocess
            cnt = path.count('\t')
            for i in range(cnt):path = path.replace('\t','')
            
            # print(cnt, path, stack)
            # 2. File Length
            if '.' in path:
                directory = None
                while stack and stack[-1][0] >=cnt:
                    directory = stack.pop()
                sentence = ''
                for _, string in stack:
                    sentence += string
                    sentence += '/'
                sentence += path
                answer = max(answer, len(sentence))
                # print(sentence, answer)
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


    

Solution().lengthLongestPath("dir\n        file.txt")
# Solution().lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")