class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(numbers) - 1

        while r - l > 0:
            if numbers[r] + numbers[l] == target:
                return [l + 1, r + 1]
            elif numbers[r] + numbers[l] > target:
                r -= 1
            else:
                l += 1
        return [] 
