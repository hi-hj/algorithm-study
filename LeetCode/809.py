from typing import List

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        # Function : String -> List : (Character, Count) ...
        # EX) "hello" -> [('h',1), ('e',1), ('l',2), ('o',1)]
        def countChar(string):
            result = []
            count = 1
            before = string[0]
            
            for i in range(len(string)):
                if i==len(string)-1 or string[i]!=string[i+1]:
                    result.append((string[i], count))
                    count = 1
                else:
                    count +=1
            return result
        
        # 1. Convert s
        s = countChar(s)
        answer = 0


        # 2. Iterate & Compare : word to s
        for word in words:
            word = countChar(word)
            count_check = True
            
            # 3-1. Sequence not match
            if len(s)!=len(word):
                continue
            
            for i in range(len(word)):
                wChar, wCount = word[i]
                sChar, sCount = s[i]
                
                # 3-2. Sequence not match
                # 3-3. Condition : Group should be bigger than 3
                # 3-4. word is stretchy. Not Shorten
                if wChar!=sChar or (wCount!=sCount and sCount<3) or wCount>sCount:
                    count_check = False
                    break
            if count_check:
                answer+=1
        
        return answer
        