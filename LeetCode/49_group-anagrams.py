# collections.defaultdict : 기본 값이 자동으로 부여될 수 있게
# defaultdict(list) : 기본 값을 list로 정함 []
# sorted(str) : acb -> a b c --> ''.join(sorted(str)) -> abc

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = collections.defaultdict(list)
        
        
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        
        return anagrams.values()
