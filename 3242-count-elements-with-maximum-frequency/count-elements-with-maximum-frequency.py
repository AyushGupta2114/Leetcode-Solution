class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        a=Counter(nums)
        max=-1
        for i,j in a.items():
            if j>max:
                max=j
        sum=0
        for i in a.values():
            if i==max:
                sum+=i
        return sum
        
        