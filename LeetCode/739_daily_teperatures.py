class Solution(object):
    def dailyTemperatures(self, T):
        result = [0]*len(T)
        stack = []
        for i, cur in enumerate(T):
            print(i, stack)
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                print(last)
                result[last] = i-last
            stack.append(i)
        print(result)
        return result
            



T = [73, 74, 75, 71, 69, 72, 76, 73]
Solution().dailyTemperatures(T)