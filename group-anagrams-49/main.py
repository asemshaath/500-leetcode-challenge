class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        organized_anagrams = defaultdict(list)
        letters = "abcdefghijklmnopqrstuvwxyz"
        
        for s in strs:
            count = [0] * 27
            for letter in s:
                c = letters.find(letter)
                count[c] += 1
        
            organized_anagrams[tuple(count)].append(s)

        return list(organized_anagrams.values())
    
   
