class Solution:
    def countBits(self, n: int) -> List[int]:
        k=[]
        for i in range(0,n+1):
            a=bin(i).replace("0b", "")
            count=0
            print(str(a))
            for j in str(a):
                print(j)
                if(j=='1'):
                    count+=1
            k.append(count)
        print(k)
        return k
            
        