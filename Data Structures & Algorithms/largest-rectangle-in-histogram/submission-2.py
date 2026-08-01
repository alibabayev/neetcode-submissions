class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # [(index, height), ...]
        n = len(heights)
        max_area = 0

        for right_bound in range(n+1):
            current_height = heights[right_bound] if right_bound < n else 0

            while stack and heights[stack[-1]] > current_height:
                top_height = heights[stack.pop()]
                # if we pop last element in stack then
                # left_bound will be -1 so because last element's rectangle 
                # start at the beginning of histogram
                left_bound = stack[-1] if stack else -1
                width = right_bound - left_bound - 1
                max_area = max(max_area, top_height * width)
                
            stack.append(right_bound)
        
        return max_area

