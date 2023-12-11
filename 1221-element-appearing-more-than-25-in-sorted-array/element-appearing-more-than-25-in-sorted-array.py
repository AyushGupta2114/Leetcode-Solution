class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        a=Counter(arr)
        for i,j in a.items():
            if(j>(len(arr)/4)):
                print(i)
                return i
        return i
        