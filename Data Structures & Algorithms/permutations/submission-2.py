class Solution:
    # Backtrack less optimal version - easy version
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        n = len(nums)
        pick = [False] * n

        def backtrack():
            if len(subset) == n:
                result.append(subset[:])
                return 
            
            for i in range(n):
                if not pick[i]:
                    subset.append(nums[i])
                    pick[i] = True
                    backtrack()
                    subset.pop()
                    pick[i] = False
        
        backtrack()
        return result