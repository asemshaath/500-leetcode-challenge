"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # build adjacency

        adj = dict()
        def build_adj(n):
            if n.val in adj:
                return
            
            adj[n.val] = [ne.val for ne in n.neighbors]
            for ne in n.neighbors:
                build_adj(ne)

        build_adj(node)
        nodes_lst = [None] + [None] * len(adj)
        
        for k in adj:
            if k in adj:
                nodes_lst[k] = Node(k)
                
        print(adj)
        print(nodes_lst)

        for k, v in adj.items():
            neighbors_ = [nodes_lst[n] for n in v]
            nodes_lst[k].neighbors = neighbors_
        
        return nodes_lst[1]
