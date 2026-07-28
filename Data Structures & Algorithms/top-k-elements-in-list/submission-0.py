import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        top_k = []

        for num, freq in freq_map.items():
            heapq.heappush(top_k, (freq, num))
            if len(top_k) > k:
                heapq.heappop(top_k)

        return [num for freq, num in top_k]