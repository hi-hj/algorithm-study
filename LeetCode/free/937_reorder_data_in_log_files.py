class Solution(object):
    def reorderLogFiles(self, logs):
        alpha = []
        digit = []
        for log in logs:
            if log.split()[1].isalpha():
                alpha.append(log)
            else:
                digit.append(log)
        alpha.sort(key = lambda x: (x.split()[1:], x.split()[0]))
        
        return alpha + digit


logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(Solution().reorderLogFiles(logs))