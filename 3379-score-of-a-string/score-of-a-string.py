class Solution:
    def scoreOfString(self, s: str) -> int:
        a=0
        for i in range(0,len(s)-1):
            # print(ord(s[i]))
            a+=abs(ord(s[i+1])-ord(s[i]))
        print(a)
        return a
        