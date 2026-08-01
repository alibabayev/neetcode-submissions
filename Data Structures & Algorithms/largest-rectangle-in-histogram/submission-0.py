class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0

        stack = [] # [[index, height], ...]

        for right, height in enumerate(heights):
            start = right
            while stack and stack[-1][1] > height:
                start, prev_height = stack.pop()
                width = right - start
                max_area = max(max_area, prev_height * width)
            
            stack.append([start, height])

        while stack:
            start, height = stack.pop()
            max_area = max(max_area, height * (len(heights) - start))
        
        return max_area
            


