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

