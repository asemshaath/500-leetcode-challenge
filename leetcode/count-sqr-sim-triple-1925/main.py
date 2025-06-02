class Solution:
    def countTriples(self, n: int) -> int:

        total = 0
        
        for i in range(1, n + 1):
            for j in range(1, n +1):
                if i != j:
                    t = sqrt(i*i + j*j)
                    if t % 1 == 0 and int(t) <= n:
                        total += 1
        return total
            
