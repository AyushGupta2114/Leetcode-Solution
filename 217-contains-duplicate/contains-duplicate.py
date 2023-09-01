class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=Counter(nums)
        for i,j in a.items():
            if(j>=2):
                return True
        return False
        