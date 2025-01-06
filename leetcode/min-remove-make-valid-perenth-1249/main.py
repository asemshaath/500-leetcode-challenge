class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # lee(t(c)o)de)
        # (l,0) (e,1) (e,2) ('(',3)
        # chars_stack = l e e    -- (e, 2)
        # parenthasis = ( ( ) ) )
        # )

        english = 'abcdefghijklmnopqrstuvwxyz'
        chars = []
        parenths = []
        parenthasis_stack = []
        to_delete = set()

        for i, c in enumerate(s):
            if c in english:
                chars.append((c,i))
            else:
                parenths.append((c,i))
        
        for p, i in parenths:
            if p == '(':
                parenthasis_stack.append((p,i))
            elif p == ')':
                if parenthasis_stack:
                    parenthasis_stack.pop()
                else:
                    to_delete.add((p,i))

        if parenthasis_stack:
            to_delete.update(parenthasis_stack)

        parenthasis = [p for p in parenths if p not in to_delete]

        res = parenthasis + chars 

        res.sort(key=lambda x: x[1])

        res_s = [c for c, i in res]
        return "".join(res_s)
        
