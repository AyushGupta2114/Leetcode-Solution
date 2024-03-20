class Solution:
    def pivotInteger(self, n: int) -> int:
        # a=0
        # b=0
        # i=1
        # x=True
        # while(x):
        #     a+=n
        #     n-=1
        #     b+=i
        #     i+=1
        #     print(a,b)
        #     if(a==b):
        #         x=False
        # print(i)

        for i in range(1,n+1):
            a=int((i*(i+1))/2)
            b=int(((n-i+1)/2)*(n+i))
            print(a,b)
            if a==b:
                return i
        return -1
            


        