class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        print(s)
        # ab=3
        # x=[p for p in s]
        # while(ab>0):
        #     a=x.pop()
        #     x.insert(0,a)
        #     print(x)
        #     if(''.join(x)==s):
        #         return True
        #     ab-=1
        return s in (s+s)[1:-1]
        # return False

        
        