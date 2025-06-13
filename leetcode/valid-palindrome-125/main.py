class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1
        english = 'abcdefghijklmnopqrstuvwxyz0123456789'

        while R - L >= 0:
            if s[R].lower() not in english:
                R -= 1
                continue

            if s[L].lower() not in english:
                L += 1
                continue

            if s[L].lower() != s[R].lower():
                return False

            R -= 1
            L += 1
        
        return True 
