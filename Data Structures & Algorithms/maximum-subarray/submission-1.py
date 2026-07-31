class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_sum = nums[0]
        cur_sum = nums[0]

        for i in range(1, len(nums)):
            # we always check whether previous part's sum is negative
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += nums[i] 
            max_sum = max(max_sum, cur_sum)
        return max_sum

