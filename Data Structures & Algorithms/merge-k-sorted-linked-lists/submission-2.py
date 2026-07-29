# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        interval = 1

        while interval < len(lists):
            for first in range(0, len(lists) - interval, interval * 2):
                second = first + interval

                lists[first] = self.merge_two_lists(lists[first],lists[second])

            interval *= 2

        return lists[0]

    def merge_two_lists(self, first: Optional[ListNode], second: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while first and second:
            if first.val <= second.val:
                tail.next = first
                first = first.next
            else:
                tail.next = second
                second = second.next

            tail = tail.next

        tail.next = first if first else second

        return dummy.next