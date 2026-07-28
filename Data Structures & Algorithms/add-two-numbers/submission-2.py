# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2

        dummy = ListNode(0)
        cur = dummy
        carry = 0

        while p1 or p2:
            sum = carry
            if p1:
                sum += p1.val
                p1 = p1.next
            if p2:
                sum += p2.val
                p2 = p2.next
            cur.next = ListNode(sum % 10)
            carry = sum // 10
            cur = cur.next

        if carry:
            cur.next = ListNode(1)
        
        return dummy.next



            