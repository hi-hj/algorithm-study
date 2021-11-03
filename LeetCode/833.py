class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        s = list(s)
        
        k = len(indices)
        replace = []
        
        for i in range(k):
            indice, source, target = indices[i], sources[i], targets[i]
            if s[indice:indice+len(source)] == list(source):
                replace.append((indice, indice+len(source), target))
        
        for start, end, target in replace:
            for i in range(start, end): s[i] = "-"
            s[start] = target
        
        s = ''.join(s).replace("-","")
        return s