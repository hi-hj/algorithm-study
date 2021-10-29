import re
from collections import Counter

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        paragraph = [word for word in re.sub('[^\w]',' ',paragraph).lower().split()
                        if word not in banned]
        para_cnt = Counter(paragraph)
        return para_cnt.most_common(1)[0][0]

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(Solution().mostCommonWord(paragraph,banned))