class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        c=0
        b=sorted(heights)
        # heights.sort()
        for i in range(0,len(heights)):
            if heights[i]!=b[i]:
                c+=1
        return c
        
        