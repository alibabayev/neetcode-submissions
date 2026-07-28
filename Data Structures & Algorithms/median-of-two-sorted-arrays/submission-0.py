class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        total = len(nums1) + len(nums2)

        left = 0
        right = len(nums1)

        half = (total + 1) // 2

        while left <= right:
            mid = (left + right) // 2

            first_partition = mid
            second_partition = half - mid

            first_left_max = nums1[first_partition - 1]  if first_partition > 0 else float("-infinity")
            first_right_min = nums1[first_partition] if first_partition < len(nums1) else float("infinity")

            second_left_max = nums2[second_partition - 1] if second_partition > 0 else float("-infinity")
            second_right_min = nums2[second_partition] if second_partition < len(nums2) else float("infinity")
        
            if first_left_max <= second_right_min and second_left_max <= first_right_min:
                if total % 2:
                    return max(first_left_max, second_left_max)
                
                left_max = max(first_left_max, second_left_max)
                right_min = min(first_right_min, second_right_min)

                return (left_max + right_min) / 2
            
            if first_left_max > second_right_min:
                right = mid - 1
            else:
                left = mid + 1