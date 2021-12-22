from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
         
        # BFS : TimeLimit
        if endWord not in wordList:
            return 0
        n = len(beginWord)
        all_combo_dict = defaultdict(list)
        
        for word in wordList:
            for i in range(n):
                all_combo_dict[word[:i]+"*"+word[i+1:]].append(word)
        
        queue = deque()
        queue.append((beginWord, 1))
        visited = {beginWord}
        
        while queue:
            current_word, level = queue.popleft()
            for i in range(n):
                intermediate_word = current_word[:i]+"*"+current_word[i+1:]
                
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level+1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level+1))
                all_combo_dict[intermediate_word] = []
        return 0