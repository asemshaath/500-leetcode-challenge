class Node:
    def __init__(self, key=0, val=0):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
    
    # for debugging purposes
    def __str__(self):
        return f"[{self.key},{self.val}]->{self.next}"


class LRUCache:

    """
    capacity=3
    insert [1,1]
    1:1
    1

    insert [2,2]
    1:1
    2:2
    1<->2

    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict() #key point to node
        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:

        if self.cache.get(key):
            self.remove_node(self.cache[key])
            self.add_node(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        
        if self.cache.get(key):
            self.remove_node(self.cache[key])
            self.cache[key] = Node(key, value) 
            self.add_node(self.cache[key])
        else:
            self.add_node(Node(key, value))
            self.cache[key] = self.right.prev

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.cache.pop(lru.key)
            self.remove_node(lru)
        
    # head<->[]<->[removethis]<->[]<->tail
    def remove_node(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev        
    

    # []<->[addhere]<->tail
    def add_node(self, node):
        tail = self.right
        prev = self.right.prev

        node.prev = prev
        node.next = tail
        tail.prev = node
        prev.next = node 
        
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
