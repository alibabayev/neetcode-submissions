class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_min = nums[0]
        current_max = nums[0]
        max_product = nums[0]
        
        for i in range(1, len(nums)):
            prev_min = current_min
            prev_max = current_max

            current_min = min(
                nums[i],
                prev_min * nums[i],
                prev_max * nums[i]
            )

            current_max = max(
                nums[i],
                prev_min * nums[i],
                prev_max * nums[i]
            )

            max_product = max(max_product, current_max)
        
        return max_product
