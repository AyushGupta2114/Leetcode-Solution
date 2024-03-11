class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        intersection = list(nums1_set.intersection(nums2_set))
        return intersection

# Example usage:
#         def binary_search(arr,target):
#             left,right=0,len(arr)-1
#             while left<=right:
#                 mid=left+(right-left)//2
#                 if arr[mid]==target:
#                     return True
#                 elif arr[mid]<target:
#                     left=mid+1
#                 else:
#                     right=mid-1
#             return 0
#         if len(nums2)>len(nums1):
#             nums1,nums2=nums2,nums1
#         a=[]
#         for num in nums1:
#             if binary_search(nums2,num):
#                 if num not in a and num in nums2:
#                     a.append(num)
#         return a