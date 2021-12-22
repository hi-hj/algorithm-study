class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backSpace(string):
            stack = []
            for char in string:
                if char=='#' and stack:
                    stack.pop()
                elif char=='#' and not stack:
                    continue
                else:
                    stack.append(char)
            return stack

        return backSpace(s) == backSpace(t)