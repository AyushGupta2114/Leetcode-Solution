from typing import List
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        def binary_search(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False
        
        # Check which array is shorter for efficient searching
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        # Perform binary search on the shorter array
        for num in nums1:
            if binary_search(nums2, num):
                return num
        return -1  # If no common element found
