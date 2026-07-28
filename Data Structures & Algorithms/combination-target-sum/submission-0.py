class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        subset = []

        def backtrack(i, total):
            if total == target:
                result.append(subset.copy())
                return 
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    break
                subset.append(nums[j])
                backtrack(j, total + nums[j])
                subset.pop()
                

        backtrack(0, 0)
        return result     
        