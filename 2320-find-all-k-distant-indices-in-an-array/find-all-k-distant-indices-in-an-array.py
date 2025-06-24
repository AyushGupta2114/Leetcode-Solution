class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        pos=[]
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if((nums[j]==key) and (abs(i-j))<=k):
                
                    print(nums[j],abs(i-j))
                    pos.append(i)
                    break
        return pos