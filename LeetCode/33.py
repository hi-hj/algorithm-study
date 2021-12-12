from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number_map = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'],
                      '5':['j','k','i'], '6':['m','n','o'], '7':['p','q','r','s'],
                      '8':['t','u','v'], '9':['w','x','y','z']}
        

        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return
            
            for i in range(index, len(digits)):
                for j in number_map[digits[i]]:
                    dfs(i+1, path+j)
        
        if not digits:
            return []
        
        result = []
        dfs(0,"")
        
        return result
        