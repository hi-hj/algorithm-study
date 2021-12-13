class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper()
        s = s.replace("-","")

        result = ""
        another, first = divmod(len(s), k) 
        
        if first !=0:
            result += s[:first] +"-"
        
        for i in range(another):
            result += s[first+i*k:first+(i+1)*k] +"-"

        result = result[:-1]
        
        return result