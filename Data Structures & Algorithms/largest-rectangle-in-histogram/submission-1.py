class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0

        stack = [] # [(index, height), ...]

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                start, height = stack.pop()
                max_area = max(max_area, height * (i - start))
            
            stack.append((start, h))

        while stack:
            start, height = stack.pop()
            max_area = max(max_area, height * (len(heights) - start))
        
        return max_area
            


