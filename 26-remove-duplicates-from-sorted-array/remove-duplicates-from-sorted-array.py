class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(0,len(nums)-1):
            if(nums[i]==nums[i+1]):
                del nums[i:i+1]
                return  self.removeDuplicates(nums)
                break
        