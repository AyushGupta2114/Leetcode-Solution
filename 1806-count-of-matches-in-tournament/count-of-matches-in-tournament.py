class Solution:
    def numberOfMatches(self, n: int) -> int:
        mat=0
        while(n!=1):
            if(n%2==0):
                mat+=n//2
                n=n//2
                # print(n)
            else:
                mat+=(n-1)//2
                n=((n-1)//2)+1
        return mat