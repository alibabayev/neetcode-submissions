class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        remove_count = 0
        intervals.sort()
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if prev_end > start:
                remove_count += 1
                prev_end = min(prev_end, end)
            else:
                prev_end = end

        return remove_count
