class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        a=Counter(nums)
        print(a)
        max=-1
        for i,j in a.items():
            if j>max:
                max=j
        print(a.values())
        sum=0
        for i in a.values():
            print(i)
            if i==max:
                sum+=i
        print(max) 
        return sum
        
        