import random

class RandomizedSet:

    """
    init
    {}
    []
    size = 0

    insert 12
    {12:0}
    [12]
    size = 1

    insert 5
    {12:0, 5:1}
    [12,5]
    size = 2

    insert 7
    {12:0, 5:1, 7:2}
    [12,5,7]
    size = 3

    insert 88
    {12:0, 5:1, 7:2, 88:3}
    [12,5,7,88]
    size = 4

    remove 5
    {12:0, 7:2, 88:1} 
    [12,88,7]
    size = 3
    """
    def __init__(self):
        self.the_set = {}
        self.tracker = []
        self.size = 0


    def insert(self, val: int) -> bool:
        if val in self.the_set:
            return False
        self.the_set[val] = self.size
        self.size += 1
        self.tracker.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.the_set:
            return False
        # swap the last index to the index of deleted item
        self.tracker[self.the_set[val]] = self.tracker[-1]
        self.the_set[self.tracker[-1]] = self.the_set[val]
        del self.tracker[-1]
        
        del self.the_set[val]

        self.size -= 1
        return True


    def getRandom(self) -> int:
        return random.choice(self.tracker)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# obj.insert(0)
# obj.insert(1)
# print(obj)
# obj.remove(0)
# obj.insert(2)
# obj.remove(1)
# param_3 = obj.getRandom()
# print(param_3)