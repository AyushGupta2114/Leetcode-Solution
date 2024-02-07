class Solution:
    def frequencySort(self, s: str) -> str:
        a=Counter(s)
        b=dict(sorted(a.items(), key=lambda x:x[1], reverse=True))
        print(b)
        x=""
        for i,j in b.items():
            print(i,j)
            for k in range(0,j):
                x+=i
        return x
        