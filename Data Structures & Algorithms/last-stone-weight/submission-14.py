class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_weight = max(stones)
        bucket = [0] * (max_weight + 1)

        for stone in stones:
            bucket[stone] += 1

        weight = max_weight
        
        while weight > 0:
            bucket[weight] = bucket[weight] % 2
            if bucket[weight] == 0:
                weight -= 1
                continue
            
            next_weight = weight - 1

            while next_weight > 0 and bucket[next_weight] == 0:
                next_weight -= 1
            
            if next_weight == 0:
                return weight
            
            bucket[next_weight] -= 1
            
            difference = weight - next_weight
            bucket[difference] += 1

            weight = max(next_weight, difference)
            
        return 0
        
        