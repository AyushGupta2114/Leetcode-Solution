class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        k=len(s)/2
        print(k)
        f=s[:int(k)]
        g=s[int(k):]
        print(f)
        j=['a','e','i','o','u','A','E','I','O','U']
        count1=0
        count2=0
        for i in f:
            if(i in j):
                count1+=1
        for i in g:
            if(i in j):
                count2+=1
        if(count1==count2):
            return True
        else:
            return False
            
        
        