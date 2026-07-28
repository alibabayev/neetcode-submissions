class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Bitmask version
        result = []
        subset = []
        n = len(nums)

        def backtrack(mask):
            if len(subset) == n:
                result.append(subset[:])
                return 

            for i in range(n):
                if not (mask & (1 << i)):
                    subset.append(nums[i])
                    backtrack(mask | 1 << i)
                    subset.pop()

        backtrack(0)
        return result
        