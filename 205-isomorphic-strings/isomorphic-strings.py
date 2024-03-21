class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        x=Counter(s)
        y=Counter(t)
        if(list(x.values())!=list(y.values())):
            # print(list(x.values()),list(y.values()))
            return False
        a={}
        for i in range(0,len(s)):
            if(s[i] in a):
                value=a.get(t[i])
                if (a[s[i]]!=t[i]):
                    return False
                    
            else:
                a[s[i]]=t[i]
        # print(a)
        return True

        