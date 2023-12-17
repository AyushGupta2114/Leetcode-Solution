class Solution:
    def sortVowels(self, s: str) -> str:
        k=[str(i) for i in s]
        # print(k)
        a=['a','e','i','o','u','A','E','I','O','U']
        b=[]
        for i in s:
            if i in a:
                b.append(i)
        b.sort()
        for i in range(0,len(k)):
            if k[i] in a:
                # print(a[i],b[0])
                k[i]=b[0]
                b.remove(b[0])
        return ''.join(k)



        