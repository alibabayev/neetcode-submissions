class Solution:
    def reverse(self, x: int) -> int:
        if x == -2**31:
            return 0
            
        INT_MAX = 2**31 - 1
        result = 0
        is_negative = x < 0
        
        if is_negative:
            x = -x
            
        while x > 0:
            digit = x % 10
            x //= 10
            
            if result > (INT_MAX - digit) // 10:
                return 0
            
            result = result * 10 + digit
        
        return -result if is_negative else result