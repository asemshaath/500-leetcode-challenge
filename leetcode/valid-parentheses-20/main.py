class Solution:
    def isValid(self, s: str) -> bool:
        
        parenthasis = {"(":")", "[":"]", "{":"}"}
        stack = []

        for c in s:
            if c in parenthasis.keys():
                stack.append(c)
            elif c in parenthasis.values() and stack:
                top = stack.pop()
                if parenthasis[top] != c:
                    return False
            else:
                return False
        
        return len(stack) == 0


