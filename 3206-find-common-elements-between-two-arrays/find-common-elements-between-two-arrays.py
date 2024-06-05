class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        left=0
        right=0
        for i in nums1:
            if i in nums2:
                left+=1
        print(left)
        for i in nums2:
            if i in nums1:
                right+=1
        return [left,right]
        