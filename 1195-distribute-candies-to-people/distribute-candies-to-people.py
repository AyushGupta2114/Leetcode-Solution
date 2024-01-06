class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        a=[0]*num_people
        i=0
        k=1
        while(candies>0):
            if(i==len(a)):
                i=0
            if(k<=candies):
                a[i]=k+a[i]
                candies-=k
                k+=1
            else:
                a[i]+=candies
                break
            i+=1
        return a


        