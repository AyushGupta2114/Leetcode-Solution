class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        a=[]
        for i in paths:
            a.append(i[0])
        print(a)
        for i in paths:
            if i[1] not in a:
                return i[1]

        