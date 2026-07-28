class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def backtracking(idx, total):
            if total == target:
                res.append(subset.copy())
                return
            
            for i in range(idx, len(candidates)):
                if total + candidates[i] > target:
                    break
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                subset.append(candidates[i])
                backtracking(i + 1, total + candidates[i])
                subset.pop()
        
        backtracking(0, 0)
        return res