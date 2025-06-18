class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        print(nums)
        nums.sort()
        print(nums)
        a=[]
        for i in range(0,len(nums),3):
            print(nums[i],nums[i+1],nums[i+2])
            print(nums[i+2]-nums[i]>2)
            print((nums[i+1]-nums[i]>2))
            if(nums[i+2]-nums[i]>k) or (nums[i+1]-nums[i]>k):
                return []
            else:
                a.append(nums[i:i+3])
        print(a)

        return a