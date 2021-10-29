from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        result = defaultdict(list)
        for word in strs:
            result[''.join(sorted(word))].append(word)
        return result.values()

strs = ["eat","tea","tan","ate","nat","bat"]
Solution().groupAnagrams(strs)