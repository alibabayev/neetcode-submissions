class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        for right, number in enumerate(nums):
            left = right - k + 1

            # remove expired indexes from the front of the q
            if q and q[0] < left:
                q.popleft()
            
            # remove the values that are inside window,
            # but is smaller than right value
            # because they cannot be max elements inside the window
            # until right larger value exists inside the window
            # so they are safe to remove to protect monotonic decreasing q
            while q and nums[q[-1]] <= nums[right]:
                q.pop()
            
            q.append(right)

            # after first window build complete,
            # start to add max elements of each window to the result array
            if left >= 0:
                res.append(nums[q[0]])
        
        return res

        

            
