class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        a=[]
        for i in range(0,len(nums),3):
            if(nums[i+2]-nums[i]>k) or (nums[i+1]-nums[i]>k):
                return []
            else:
                a.append(nums[i:i+3])

        return a