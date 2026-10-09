class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        
        """
        letters = 'abcdefghijklmnopqrstuvwxyz'
        
        occ_s = [0] * len(letters)
        occ_t = [0] * len(letters)
        
        for c in s:
            occ_s[ord(c)-ord('a')] += 1
        
        for c in t:
            occ_t[ord(c)-ord('a')] += 1


        return occ_s == occ_t
            


