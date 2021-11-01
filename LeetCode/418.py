from typing import List
from collections import deque
import pprint
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        words = deque()
        for word in sentence:
            words.append(len(word))
        
        answer = 0
        cnt = 0 
        screen = 0

        while cnt < rows:
            word = words.popleft()
            answer +=1

            if word + screen < cols:
                screen += word+1
            elif word + screen == cols:
                cnt+=1
                screen = 0
            elif word + screen > cols:
                cnt+=1
                screen = 0
                answer -=1
                words.appendleft(word)
                continue



            words.append(word)

        return answer//len(sentence)



Solution().wordsTyping(["hello","world"], 2, 8)
Solution().wordsTyping(["a","bcd","e"], 3, 6)
Solution().wordsTyping(["i","had","apple","pie"], 4, 5)
Solution().wordsTyping(["ab","cde","f"],3, 5)
Solution().wordsTyping(["f","p","a"], 8,7)
Solution().wordsTyping(["a"], 10000, 10000)