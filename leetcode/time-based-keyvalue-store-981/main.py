class TimeMap:

    def __init__(self):
        self.mydict = dict()
        
        """
        keys:
        10:love
        20:love

        mydict:
        love10:high
        love20:low
        """
    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.mydict.get(key):
            self.mydict[key].append((value, timestamp))
        else:
            self.mydict[key] = [(value, timestamp)]        

    def get(self, key: str, timestamp: int) -> str:
        """
        ["foo", 1], ["foo", 3], ["foo", 6], ["foo", 11], ["foo", 13]
                                              l               r
        """
        res = ""
        if not self.mydict.get(key):
            return res
        
        l, r = 0, len(self.mydict.get(key)) - 1

        while r >= l:
            m = (l+r) // 2
            if self.mydict[key][m][1] > timestamp:
                r = m - 1
            elif self.mydict[key][m][1] <= timestamp:
                res = self.mydict[key][m][0]
                l = m + 1
            else:
                break
            
        if l == r:
            res = self.mydict[key][l][0]
        

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
