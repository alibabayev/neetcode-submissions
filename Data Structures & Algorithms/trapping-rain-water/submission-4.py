class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        water = 0
        n = len(height)

        left = 0
        right = n - 1

        left_max = height[0]
        right_max = height[n-1]

        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                right -= 1
        return water





        
        
        # water += min(left_max[i], right_max[i]) - height[i]

        return water  