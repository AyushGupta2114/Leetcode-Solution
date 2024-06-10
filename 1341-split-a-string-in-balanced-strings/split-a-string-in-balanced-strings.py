class Solution:
    def balancedStringSplit(self, s: str) -> int:
        a=0
        b=0
        c=0
        for i in s:
            if i=='R':
                a+=1
            else:
                b+=1
            if(a==b):
                c+=1
        return c
        
        