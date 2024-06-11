class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        b=[]
        for i in arr2:
            if i not in arr1:
                arr1.remove(i)
        # print(a)
        arr1.sort()
        for i in arr2:
            while(i in arr1):
                b.append(i)
                arr1.remove(i)
        # print(b)
        # print(arr1)
        return b+arr1


        

        