class Solution:
    # "aabca"
    # {'a': 3, 'b': 1, 'c': 1}
    
    def countPalindromicSubsequence(self, s: str) -> int:
        english = 'abcdefghijklmnopqrstuvwxyz'
        palindromics = set()

        for i, c in enumerate(s):
            left = s[0:i]
            right = s[i+1::]

            # print(f"i = {i} at {c}")
            # print(left, right)
            for e in english:
                if e in left and e in right:
                    palindromics.add((c,e))
        
        return len(palindromics)

