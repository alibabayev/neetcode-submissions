class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        stack = []
        water = 0
        
        for right in range(len(height)):
            while stack and height[stack[-1]] < height[right]:
                bottom = height[stack.pop()]
                if not stack:
                    break
                    
                left = stack[-1]

                width = right - left - 1
                area_height = min(height[left], height[right]) - bottom
                
                water += width * area_height
            stack.append(right)

        return water
