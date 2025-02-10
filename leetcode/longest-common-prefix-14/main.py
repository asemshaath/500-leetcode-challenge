    def longestCommonPrefix(self, strs: List[str]) -> str:
        p = 0
        move_p = True

        while move_p:
            if p < len(strs[0]):
                pc = strs[0][p]
            else:
                break
            for s in strs:
                if p >= len(s):
                    move_p = False
                    break
                if s[p] != pc:
                    move_p = False
            if move_p:
                p += 1

        return strs[0][:p]

