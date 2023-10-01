class Solution:
    def reverseWords(self, s: str) -> str:
        x=s.split()
        lis=[]
        for i in x:
            i=i[::-1]
            lis.append(i)
        y=(" ".join(lis))
        return y