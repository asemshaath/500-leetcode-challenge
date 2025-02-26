class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        enc = [f"{len(s)}#{s}" for s in strs]
        return "".join(enc)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0

        # leet code
        # 0123456789
        # 4#leet4#code
        while i < len(s):
            length = ''
            while s[i] != '#':
                length += s[i]
                i += 1
            length = int(length)
            res.append(s[i+1:i+length+1])
            i += length + 1

        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
