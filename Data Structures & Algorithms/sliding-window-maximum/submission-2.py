class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        res = []

        for right, number in enumerate(nums):
            left = right - k + 1

            heapq.heappush(max_heap, [-1 * number, right])

            while max_heap[0][1] < left:
                heapq.heappop(max_heap)
        
            if left >= 0:
                res.append(-1 * max_heap[0][0])

        return res