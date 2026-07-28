class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
    
        def backtrack(wall_index):
            if wall_index == n:
                result.append(nums[:])
                return 
            
            for candidate_index in range(wall_index, n):
                nums[wall_index], nums[candidate_index] = nums[candidate_index], nums[wall_index]
                backtrack(wall_index + 1)
                nums[wall_index], nums[candidate_index] = nums[candidate_index], nums[wall_index]
        
        backtrack(0)
        return result

# Bitmask version
#     result = []
#     subset = []
#     n = len(nums)
#     # pick = [False] * n

#     def backtrack(mask):
#         if len(subset) == n:
#             result.append(''.join(subset))
#             return 
        
#         for i in range(n):
#             if not (mask & (1 << i)):
#                 subset.append(nums[i])
#                 backtrack(mask | 1 << i)
#                 subset.pop()
    
#     backtrack(0)
#     return result
    
# backtrack version
# def permute_nums(nums):
#     result = []
#     subset = []
#     n = len(nums)
#     pick = [False] * n

#     def backtrack():
#         if len(subset) == n:
#             result.append(''.join(subset))
#             return 
        
#         for i in range(n):
#             if not pick[i]:
#                 subset.append(nums[i])
#                 pick[i] = True
#                 backtrack()
#                 subset.pop()
#                 pick[i] = False
    
#     backtrack()
#     return result