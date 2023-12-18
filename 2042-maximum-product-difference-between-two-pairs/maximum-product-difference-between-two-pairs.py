class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
#         Max=0
#         Min=2147483647
#         for i in range(0,len(nums)):
#             for j in range(i+1,len(nums)):
#                 if(nums[i]*nums[j]>Max):
#                     Max=nums[i]*nums[j]
#                     print(Max)
#                 if(nums[i]*nums[j]<Min):
#                     Min=nums[i]*nums[j]
#                     print(Min)
#         print(Max)
        
#         return Max-Min
      
        nums.sort(reverse=True)
        return nums[0]*nums[1]-nums[-1]*nums[-2]
        
        
          # Min=Max
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if(nums[i]*nums[j]<Min):
        #   