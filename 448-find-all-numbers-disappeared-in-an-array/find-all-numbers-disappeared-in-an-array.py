# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         nums.sort()
#         a=[]
#         print(nums)
#         for i in range(1,len(nums)+1):
#             # print(i)
#             if(i not in nums):
#                 a.append(i)
#         return a
        
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
        return [i + 1 for i in range(n) if nums[i] > 0]
