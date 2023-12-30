class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        a="".join(words)
        if(len(words)==1):
            return True
        print(len(words))
        B=Counter(a)
        print(B)
        for i,j in B.items():
            if(j%len(words)!=0):
                return False
        return True


        