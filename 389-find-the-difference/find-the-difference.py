import numpy as np
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        list1=list(s.replace(" ",""))
        list2=list(t.replace(" ",""))
        res=[ele for ele in list2]
        for i in list1:
            if(i in list2):
                res.remove(i)
        return res[0]