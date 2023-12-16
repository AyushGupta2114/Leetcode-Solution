from itertools import permutations
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lt=[i for i in t]
        ls=[i for i in s]
        lt.sort()
        ls.sort()
        if(lt==ls):
            return True 
        return False
        