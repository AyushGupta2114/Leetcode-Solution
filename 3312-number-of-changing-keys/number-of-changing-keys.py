class Solution:
    def countKeyChanges(self, s: str) -> int:
        c=0
        s=s.lower()
        print(s.lower())
        for i in range(0,len(s)-1):
            if(s[i]!=s[i+1]):
                # print(s[i],s[i+1])
                c+=1
        return c
        