    def maxArea(self, height: List[int]) -> int:
        water = 0

        l, r = 0, len(height) - 1

        while r >= l:
            currWater = min(height[l], height[r]) * (r-l)
            water = max(currWater, water)
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return water


# new sol march 3rd, 2025
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        water = 0

        while r - l > 0:
            water = max(water, (r-l)*min(height[l], height[r]))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return water




