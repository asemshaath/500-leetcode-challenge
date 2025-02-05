class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # gas = [1,2,3,4,5], cost = [3,4,5,1,2]
        # net = [-2, -2, -2, 3, 3]

        # gas = [2,3,4], cost = [3,4,3]
        # net = [-1, -1, 1]
        
        L = len(gas)
        curr_total = 0
        starting_point = -1

        if sum(gas) - sum(cost) < 0:
            return starting_point
        
        for i in range(L):
            curr_total += gas[i] - cost[i]
            if curr_total < 0:
                starting_point = -1
                curr_total = 0
            elif starting_point == -1:
                starting_point = i
            
        return starting_point



        



