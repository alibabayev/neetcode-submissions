class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        found = 0
        
        while slow != found:
            slow = nums[slow]
            found = nums[found]
        
        return found

