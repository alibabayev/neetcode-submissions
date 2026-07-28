class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0 

        for num in numSet:
            length = 1
            if num - 1 in numSet:
                continue

            while num + 1 in numSet:
                length += 1
                num += 1
                
            res = max(res, length)
        
        return res