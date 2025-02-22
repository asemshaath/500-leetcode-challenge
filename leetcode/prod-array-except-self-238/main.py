class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        acc = 1
        prefix = [(acc := acc * n) for n in nums]
        acc = 1
        postfix = [(acc := acc * n) for n in nums[::-1]]
        postfix = postfix[::-1]
        res = []

        for i in range(len(nums)):
            pre = prefix[i - 1] if i > 0 else 1
            post = postfix[i + 1] if i < len(nums) - 1 else 1
            res.append(pre * post)
        return res

