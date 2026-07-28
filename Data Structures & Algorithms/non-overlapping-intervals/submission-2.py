class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        remove_count = 0
        intervals.sort(key = lambda x: x[1])
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if prev_end > start:
                remove_count += 1
            else:
                prev_end = end

        return remove_count
