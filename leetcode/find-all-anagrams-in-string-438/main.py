    def findAnagrams(self, s: str, p: str) -> List[int]:
        # cbaebabacd
        # 0123456789
        # english = 'abcdefghijklmnopqrstuvwxyz'

        if len(p) > len(s):
            return []

        pcount = defaultdict(lambda: 0)
        ccount = defaultdict(lambda: 0)
        l = len(p)
        res =  []

        for i in range(len(p)):
            pcount[p[i]] += 1
            ccount[s[i]] += 1
            
        if pcount == ccount:
            res.append(0)

        pointer = 0
        for i in range(len(p), len(s)):
            ccount[s[pointer]] -= 1
            ccount[s[i]] += 1
            if ccount[s[pointer]] == 0:
                ccount.pop(s[pointer])
            pointer += 1
            if ccount == pcount:
                res.append(pointer)
        return res
