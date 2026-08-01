class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        carry_bit = 0
        res = 0

        for bit_position in range(32):

            a_bit = (a >> bit_position) & 1
            b_bit = (b >> bit_position) & 1

            res_bit = a_bit ^ b_bit ^ carry_bit 

            if res_bit:
                res = res | (res_bit << bit_position)
            
            carry_bit = (
                (a_bit & b_bit)
                or
                ((a_bit ^ b_bit) & carry_bit)
            )

        return res if res <= max_int else ~(res ^ mask)
        