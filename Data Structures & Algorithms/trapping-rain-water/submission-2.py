class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        water = 0
        n = len(height)
        # left_max = [0] * n
        # right_max = [0] * n
        for i in range(n):
            # if we put zero then the left and right max values can be less than the current height
            # so then we will have negative value in calculation of water level
            # we need to find left and right max that are at least in current bar's height
            left_max = height[i] 
            right_max = height[i] 
            for j in range(i):
                left_max = max(left_max, height[j])
            
            for j in range(i + 1, n):
                right_max = max(right_max, height[j])
            
            water += min(left_max, right_max) - height[i]
        
        return water

        
        