from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        result = []

        freq_buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            freq_buckets[freq].append(num)

        for i in range(len(freq_buckets) - 1, 0, -1):
            for num in freq_buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return result
        