class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        
        for strings in strs:
            count = [0] * 26
            for characters in strings:
                count[ord(characters) - ord('a')] += 1
            res[tuple(count)].append(strings)
            
        return res.values()

#Time Complexity: O(n)
#Space Complexity: O(n)