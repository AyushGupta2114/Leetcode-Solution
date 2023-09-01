class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for i in range(0,len(matrix)):
        #     for j in range(0,len(i)):
        #         print(matrix[i][j])
        # #         if(target in j):
        # #             return True
        # # return False
        for i in matrix:
            for j in i:
                print(j)
                if(j==target):
                    return True
        return False