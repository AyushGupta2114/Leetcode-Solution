class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a=[]
        for i in s:
            if i!='#':
                a.append(i)
            elif i=='#' and len(a)!=0:
                a.pop()
        # print(a)
        ab=[]
        for i in t:
            if(i!='#'):
                ab.append(i)
            elif i=='#' and len(ab)!=0:
                ab.pop()
        print(ab)
        return a==ab
        