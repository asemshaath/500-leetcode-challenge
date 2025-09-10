class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        tracker = []

        def helper(i, tracker):
            if i >= len(nums):
                res.append(tracker.copy())
                return
                
            helper(i+1, tracker.copy())
            tracker.append(nums[i])
            helper(i+1, tracker.copy())
            tracker.pop()
        
        helper(0, tracker)
            
        return res

# new solotion (iterative)
class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for n in nums:
            tracker = []
            for el in res:
                tmp = el.copy()
                tmp.append(n)
                tracker.append(tmp)
            res.extend(tracker)
            
        return res

# Another solution after a while
class Solution3:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(lst, acc):
            if not lst:
                res.append(acc)
                return
           
            helper(lst[1:], acc + [lst[0]])
            helper(lst[1:], acc)

            

        helper(nums, [])

        return res
