class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        #  for(int i = 0 ; i < n ; i++)
        # {
        #     if(nums[i] <= prev)
        #     {
        #         cntMoves += (prev + 1) - nums[i];

        #         nums[i] = prev + 1;
        #     }

        #     prev = nums[i];
        nums.sort()
        count=0
        prev=-1
        for i in range(len(nums)):
            if (nums[i]<=prev):
                count+=(prev+1)-nums[i]
                nums[i]=prev+1
            prev=nums[i]
        return count
        # count=0
        # # nums.sort()
        # print(nums)
        # print("")
        # for i in range(0,len(nums)-1):
        #     if(nums[i]==nums[i+1]):
        #         nums[i+1]=nums[i+1]+1
        #         count+=1
        #     elif nums[i]>=nums[i+1]:
        #         nums[i+1]=nums[i]+1
        #         count+=2
        #     print(nums)
        # # print(nums)
        # return count
        
        