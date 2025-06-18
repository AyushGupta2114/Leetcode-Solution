class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(0,len(nums)-1,1):
            print(nums[i+1],nums[i])
            if (nums[i+1]%2==0):
                if(nums[i]%2==0):
                    return False
            if (nums[i+1]%2!=0):
                if(nums[i]%2!=0):
                    return False
        return True
        