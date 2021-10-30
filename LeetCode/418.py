from typing import List
from collections import deque
import pprint
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        sentence = deque(sentence)
        answer = 0
        cnt = 0 
        screen =""

        while cnt < rows:
            word = sentence.popleft()
            # print(word, "/", screen)
            answer +=1

            if len(word) + len(screen) < cols:
                screen += word
                screen += '-'
                # print("0:", screen)


            elif len(word) + len(screen) == cols:
                screen += word
                cnt+=1
                # print("1:",screen)
                screen =""

            elif len(word) + len(screen) > cols:
                cnt +=1
                screen =""
                answer -=1
                sentence.appendleft(word)
                continue
            # elif len(word) + len(screen) > cols:
            #     screen.ljust(cols,'-')
            #     cnt +=1
            #     print("2:",screen)
            #     screen =""


            sentence.append(word)

        return answer//len(sentence)



Solution().wordsTyping(["hello","world"], 2, 8)
Solution().wordsTyping(["a","bcd","e"], 3, 6)
Solution().wordsTyping(["i","had","apple","pie"], 4, 5)
Solution().wordsTyping(["ab","cde","f"],3, 5)
Solution().wordsTyping(["f","p","a"], 8,7)
Solution().wordsTyping(["a"], 10000, 10000)