class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if(val in nums):
            nums.pop(nums.index(val))
            return self.removeElement(nums,val)
        return len(nums)
            
                