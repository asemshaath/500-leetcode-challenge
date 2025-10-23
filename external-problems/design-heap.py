class MinHeap:
    
    """
           2
        4      5
      6   8  7   9
    11

    heap = [0,2,4,5,6,8,7,9,11]
    left = 2*i
    right = 2*i + 1

    2*2=4

    # easy push
    push 11

    # pop
    heap = [0,2,4,5,6,8,7,9,11]

    heap = [0,11,4,5,6,8,7,9,2]


    # example
    push 1
    heap = [0,2,4,5,6,8,7,9,11,1]
    6 is the parent
    left = 4 * 2 = 8
    right = 4 * 2 + 1 = 9
    9 // 2 = 4
    8 // 2 = 4

    """
    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        self.heap.append(val)
        curr = len(self.heap) - 1
        self._bubble_up(curr)

    def pop(self) -> int:
        if len(self.heap) <= 1:
            return -1

        res = self.heap[1]
        tmp = self.heap.pop()
    
        if len(self.heap) == 1:
            return res

        self.heap[1] = tmp
        
        self._bubble_down(1)

        return res


    def top(self) -> int:
        if len(self.heap) > 1:
            return self.heap[1]
        return -1

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums
        curr = len(self.heap) // 2

        while curr > 0:
            self._bubble_down(curr)
            curr -= 1
    
    def _bubble_up(self, curr):
        parent_indx = curr // 2
        while parent_indx > 0 and self.heap[parent_indx] > self.heap[curr]:
            tmp = self.heap[curr]
            self.heap[curr] = self.heap[parent_indx]
            self.heap[parent_indx] = tmp
            
            curr = parent_indx
            parent_indx = curr // 2
    
    def _bubble_down(self, curr):
                
        child = curr * 2

        while child < len(self.heap):
            if child + 1 < len(self.heap) and  self.heap[child] > self.heap[child+1]:
                child += 1
            
            if self.heap[child] < self.heap[curr]:
                tmp = self.heap[child]
                self.heap[child] = self.heap[curr]
                self.heap[curr] = tmp

            curr = child
            child = curr * 2

