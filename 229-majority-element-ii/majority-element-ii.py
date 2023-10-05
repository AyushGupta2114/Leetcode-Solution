import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a=Counter(nums)
        k=[]
        for i,j in a.items():
            if(j>math.floor(len(nums)/3)):
                k.append(i)
        return k

        