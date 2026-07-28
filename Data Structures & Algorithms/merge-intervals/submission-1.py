class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        result = []

        max_start = max(interval[0] for interval in intervals)
        max_ends = [-1] * (max_start + 1)

        for start, end in intervals:
            max_ends[start] = max(max_ends[start], end)

        start = 0
        while max_ends[start] == -1:
            start += 1
        
        end = max_ends[start]

        for curr_start in range(start + 1, max_start + 1):
            if max_ends[curr_start] != -1:
                if curr_start <= end:
                    end = max(end, max_ends[curr_start])
                else:
                    result.append([start, end])
                    start = curr_start
                    end = max_ends[curr_start]
        
        result.append([start, end])
        
        return result
        