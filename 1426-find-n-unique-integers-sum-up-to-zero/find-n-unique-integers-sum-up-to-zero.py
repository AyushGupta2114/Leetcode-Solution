class Solution:
    def sumZero(self, n: int) -> List[int]:
        if(n%2==0):
            z=[]
        elif(n==1):
            return [0]
        else:
            z=[0]
        for i in range(1,n+1):
            if(len(z)==n):
                return z
            z.append(i)
            z.append(-i)
        print(z)
        return []


        