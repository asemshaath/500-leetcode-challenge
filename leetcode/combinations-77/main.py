class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        curr = []

        def helper(i, curr):

            if len(curr) == k:
                res.append(curr)
                return
            if i > n:
                return
            
            helper(i + 1, curr.copy())
            curr.append(i)
            helper(i + 1, curr.copy())
            curr.pop()
        
        helper(1, curr)
        return res
