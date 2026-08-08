class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        accepted = set()
        
        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            
            if a == target[0]:
                accepted.add(0)
            
            if b == target[1]:
                accepted.add(1)

            if c == target[2]:
                accepted.add(2)

        return len(accepted) == 3
            

        