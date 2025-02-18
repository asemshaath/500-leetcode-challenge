class Allocator:

    def __init__(self, n: int):
        self.memory = [0 for _ in range(n)]
        self.n = n

    def allocate(self, size: int, mID: int) -> int:
        availible = 0
        for i in range(self.n):
            if self.memory[i] == 0:
                availible += 1
            else:
                availible = 0
            
            if availible == size:
                for j in range(i - size + 1, i + 1):
                    self.memory[j] = mID
                return i - size + 1
        return -1

    def freeMemory(self, mID: int) -> int:
        freed = 0
        for i in range(self.n):
            if self.memory[i] == mID:
                self.memory[i] = 0
                freed += 1
        
        return freed


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)
