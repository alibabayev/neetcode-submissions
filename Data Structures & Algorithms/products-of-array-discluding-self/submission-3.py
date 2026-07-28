class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        preprod = 1
        postprod = 1
        res = [1] * n

        for i in range(n):
            res[i] = preprod
            preprod *= nums[i]

        for i in range(n-1, -1, -1):
            res[i] *= postprod
            postprod *= nums[i]
        
        return res
        

         