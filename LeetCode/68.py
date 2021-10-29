from typing import List
from collections import deque

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        words = deque(words)
        answer = []
        length = 0
        now = []

        while words:
            word = words.popleft()
            # ADD
            if length + len(word) <=maxWidth:
                now.append(word)
                length += (len(word)+1)
            
            # NOT ADD
            else:
                words.appendleft(word)
                if len(now)==1:
                    sentence = now[0].ljust(maxWidth, " ")
                else:
                    sentence = ""
                    space = maxWidth - length + len(now)
                    space_count = []
                    count = len(now) -1
                    
                    a,b = divmod(space, count)
                    for i in range(count):
                        if b>0:
                            space_count.append(a+1)
                            b-=1
                        else:
                            space_count.append(a)
                    space_count.append(0)


                    for w, s in zip(now, space_count):
                        sentence+=w
                        sentence+=(' '*s)


                answer.append(sentence)
                length = 0
                now = []
        
        # LAST SENTENCE
        if now:
            sentence =""
            for word in now:
                sentence +=(word +" ")
            sentence = sentence[:-1]
            sentence = sentence.ljust(maxWidth," ")


            answer.append(sentence)

        return answer
            
                

    


# Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."],16)
# Solution().fullJustify(["What","must","be","acknowledgment","shall","be"], 16)
# Solution().fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20)