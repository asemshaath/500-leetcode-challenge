from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        L = len(nums)
        occurances = defaultdict(int)
        res = []

        # nums = [1,1,1,2,2,3]
        # occurances = [0, 3, 2, 1]

        for i in range(L):
            occurances[nums[i]] += 1

        # print(list(occurances.items()))
        # print(max(occurances.items(), key = operator.itemgetter(1)))
        while k > 0:
            
            key, v = max(occurances.items(), key = operator.itemgetter(1))
            
            occurances[key] = 0
            res.append(key)
            k -= 1

        return res



# new sol using heaps


class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        occ = {}

        for n in nums:
            if n not in occ:
                occ[n] = 1
            else:
                occ[n] += 1
        

        oc = list(occ.items())
        h = []
        # print(h)
      
        
        for n, c in oc:
            heappush(h, (c, n))
            if len(h) > k:
                heappop(h)
        
        res = [n for _, n in h]
        return res







