from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        0: 1
        1: 0, 2
        2: 1
        3: 4
        4: 3

        v = {0}
        q = [0, 1, 2]
        """
        
        adj = dict()
        v = set()
        q = deque()
        res = 0

        # build adjancency dict
        for x, y in edges:
            if adj.get(x):
                adj[x].append(y)
            else:
                adj[x] = [y]
            
            if adj.get(y):
                adj[y].append(x)
            else:
                adj[y] = [x]

        for k in range(n):
            if k not in v:
                q.append(k)
                while q:
                    node = q.pop()
                    if node not in v:
                        v.add(node)
                        neighbors = adj.get(node, [])
                        neighbors = [n for n in neighbors if n not in v]
                        for n in neighbors:
                            q.append(n)
                res += 1
        
        return res

