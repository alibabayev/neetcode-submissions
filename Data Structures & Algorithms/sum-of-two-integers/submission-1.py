class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        carry = 0
        while b != 0:
            sum_without_new_carries = (a ^ b) & mask
            carry = ((a & b) & mask) << 1

            a = sum_without_new_carries
            b = carry
        
        # result is positive number
        if a <= max_int:
            return a 
        
        return ~(a ^ mask)
        
        