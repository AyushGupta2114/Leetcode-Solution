class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1=Counter(nums1) 
        dict2=Counter(nums2) 
        commonDict = dict1 & dict2 
        commonChars = list(commonDict.elements()) 
        commonChars = sorted(commonChars) 
        return commonChars