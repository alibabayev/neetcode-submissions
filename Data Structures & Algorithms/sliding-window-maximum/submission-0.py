class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        

        for right, number in enumerate(nums):
            left = right - k + 1

            if q and q[0] < left:
                q.popleft()
            
            while q and nums[q[-1]] <= nums[right]:
                q.pop()
            
            q.append(right)

            if left >= 0:
                res.append(nums[q[0]])
        
        return res

        

            
