class Solution:
    def largestOddNumber(self, num: str) -> str:
        return num.rstrip('02468')

        
        # a=[int(i) for i in num]
        # m=0
        # for i in a:
        #     if(i%2!=0):
        #         m+=1
        # if(m==0):
        #     return ""
        # n=""
        # for i in range(0,len(a)-1):
        #     n=n+str(a[i])
        #     if(int(n)%2==0 and a[i+1]%2==0):
        #         if(int(n)%2==0 and int(num)%2==0):
        #             continue
        #         else:
        #             return n
        # return n




        # # if(num=="10133890"):
        # #     return "1013389"
        # # if(int(num)%2!=0):
        # #     return num
        # # a=[int(i) for i in num]
        # # print(a)
        # # max=-1
        # # for i in a:
        # #     if(i%2!=0):
        # #         if(i>int(max)):
        # #             max=str(i)
        # # if max==-1:
        # #     return ""
        # # else:
        # #     return max