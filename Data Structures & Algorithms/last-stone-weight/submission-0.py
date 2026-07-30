class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)

            # since s1 and s2 are negative values of original stones
            if s1 < s2:
                heapq.heappush(stones, s1 - s2)
        
        return abs(stones[0]) if len(stones) else 0

