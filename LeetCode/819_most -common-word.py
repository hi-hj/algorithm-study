# 전처리 -정규식
# \w : 단어 문자 (word character), ^ : not
# dict의 most_common 활용
# collections.Counter(words).most_common(1) : 가장 흔한 수


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
                    if word not in banned]
        #print(words)
        
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]
        