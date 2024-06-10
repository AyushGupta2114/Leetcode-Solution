class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            if len(str(nums[i]))%2==0:
                count+=1
        return count         

        # a={}
        # for i in nums:
        #     n=i
        #     count=0
        #     while(i>0):
        #         i=i//10
        #         count+=1
        #     a[n]=count
        # # print(a)
        # k=0
        # for i,j in a.items():
        #     if(j%2==0):
        #         k+=1
        # return k
        