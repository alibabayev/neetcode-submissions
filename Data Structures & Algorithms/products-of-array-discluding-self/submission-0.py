class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zero_count = 0
        prod = 1
        
        # find product of non-zero values, and find number of zeros in array
        for num in nums:
            if num: # number is not zero 
                prod *= num 
            else:
                zero_count += 1
        
        # if there are more than one zero values then all output array will be zeros
        if zero_count > 1:
            return [0] * n
        
        output = [0] * n
        for i, num in enumerate(nums):
            # if there is only one zero, then the array will have product value only on that cell, and zeros in all other cells
            if zero_count:
                output[i] = 0 if num else prod
            else: # if all are non-zero then do normal division
                output[i] = prod // num
        
        return output
    

