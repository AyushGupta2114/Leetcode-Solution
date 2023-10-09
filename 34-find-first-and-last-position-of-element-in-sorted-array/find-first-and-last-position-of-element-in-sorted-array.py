class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if(len(nums)==1):
            if(nums[0]==target):
                return [0,0]
        # else if()
        List=[]
        for i in range(0,len(nums)):
            if(nums[i]==target):
               List.append(i)
        Z=len(List)  
        if(Z==0):
            return [-1,-1]
        elif(Z==1):
            return [List[0],List[0]]
        else:
            return [List[0],List[len(List)-1]]