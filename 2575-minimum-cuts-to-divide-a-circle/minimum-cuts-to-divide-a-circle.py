class Solution:
    def numberOfCuts(self, n: int) -> int:
        if(n%2==0):
            return n//2
        elif n==1:
            return 0
        else:
            return n
        