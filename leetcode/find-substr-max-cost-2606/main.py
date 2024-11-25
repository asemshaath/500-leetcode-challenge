    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        english = ' abcdefghijklmnopqrstuvwxyz'
        sints = []

        for c in s:
            if c in chars:
                i = chars.find(c)
                sints.append(vals[i])
            else:
                i = english.find(c)
                sints.append(i)
        
        # kadanes shits 
        maxim = 0
        curr = 0

        for n in sints:
            if curr < 0:
                curr = 0
            
            curr += n
            if curr > maxim:
                maxim = curr
        
        return maxim

