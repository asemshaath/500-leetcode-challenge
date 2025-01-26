class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0

        for n in s:
            if n - 1 not in s:
                curr_res = 1
                curr_num = n

                while curr_num in s:
                    res = max(res, curr_res)
                    curr_num += 1
                    curr_res += 1
        return res
