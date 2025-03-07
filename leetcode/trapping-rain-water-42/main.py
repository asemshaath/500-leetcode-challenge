class Solution:
    def trap(self, height: List[int]) -> int:
        L = len(height)
        water = [0] * L
        left = [0] * L
        right = [0] * L
        
        left[0] = height[0]
        for i in range(1, L):
            # mx = max(height[i], mx)
            left[i] = max(height[i], left[i-1])
        
        right[L - 1] = height[L - 1]
        for i in reversed(range(L-1)):
            # mxr = max(height[i], mxr)
            right[i] = max(height[i], right[i+1])
        
        for i in range(L):
            w = min(left[i], right[i]) - height[i]
            water[i] = w if w >=0 else 0

        return sum(water) 
