class Solution:
    def isHappy(self, n: int) -> bool:
        sum1=0
        while(sum1!=1):
            if(n==1):
                return True
            if(n > 1 and n <= 6):
                return False
            sum1=0
            while(n!=0):
                sum1=sum1+(n%10)**2
                n=n//10
            if(sum1==1):
                return True
            n=sum1

            
                
        