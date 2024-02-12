from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1=Counter(nums)
        print(dict1)
        for i,k in dict1.items():
            if(k>(len(nums)/2)):
                z=i
        return z
        