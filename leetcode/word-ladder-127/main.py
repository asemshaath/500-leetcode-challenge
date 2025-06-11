class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        patterns = dict()

        # build patterns
        for s in wordList:
            for i, c in enumerate(s):
                t_s = s[:i] + '*' + s[i+1:]
                if t_s in patterns:
                    patterns[t_s].append(s)
                else:
                    patterns[t_s] = [s]
        
        v = set()
        q = deque([beginWord])
        res = 1

        while q:
            for _ in range(len(q)):  # Process the current level

                w = q.popleft()
                if w == endWord:
                    return res
                if w not in v:
                    v.add(w)
                    for i, c in enumerate(w):
                        t_s = w[:i] + '*' + w[i+1:]
                        if patterns.get(t_s):
                            for wr in patterns.get(t_s):
                                if wr not in v:
                                    q.append(wr)
            res += 1

            

        print(patterns)
        return 0
