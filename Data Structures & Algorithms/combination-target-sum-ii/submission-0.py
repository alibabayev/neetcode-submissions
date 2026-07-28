class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def backtracking(idx, total):
            if total == target:
                res.append(subset.copy())
                return
            
            if idx >= len(candidates) or total > target:
                return
            
            subset.append(candidates[idx])
            backtracking(idx + 1, total + candidates[idx])
            subset.pop()

            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1
            backtracking(idx + 1, total)
        
        backtracking(0, 0)
        return res