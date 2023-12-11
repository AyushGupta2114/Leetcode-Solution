class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        for i in range(0,len(arr)):
            if arr.count(arr[i]) > (len(arr)/4):
                return arr[i]
        # a=Counter(arr)
        # for i,j in a.items():
        #     if(j>(len(arr)/4)):
        #         print(i)
        #         return i
        # return i
        