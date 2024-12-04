class MinStack:
    """
    [1,2,-2,7]
    {
        0:-inf,
        1:1,
        2:1,
        3:-2,
        4:-2,
    }
    """
    def __init__(self):
        self.stack = []
        self.min_dict = dict()
        self.min_dict[0] = sys.maxsize - 1
        self.size = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        pre_size = self.size
        self.size += 1
        # print(f"push called - val:{val}")
        # print(self.min_dict)
        if val < self.min_dict[pre_size]:
            self.min_dict[self.size] = val
        else:
            temp = self.min_dict[pre_size]
            self.min_dict[self.size] = temp


    def pop(self) -> None:
        del self.stack[self.size - 1]
        pre_size = self.size
        self.size -= 1
        self.min_dict.pop(pre_size)

    def top(self) -> int:
        return self.stack[self.size - 1]

    def getMin(self) -> int:
        # print("getMin is called")
        # print(self.min_dict)

        return self.min_dict[self.size]
