class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        nums.sort()

        def backtrack(wall_index):
            if wall_index == n:
                result.append(nums[:])
                return

            for i in range(wall_index, n):
                if i > wall_index and nums[i] == nums[wall_index]:
                    continue
                nums[wall_index], nums[i] = nums[i], nums[wall_index]
                backtrack(wall_index + 1)

            for i in range(n - 1, wall_index, -1):
                nums[wall_index], nums[i] = nums[i], nums[wall_index]

        backtrack(0)
        return result