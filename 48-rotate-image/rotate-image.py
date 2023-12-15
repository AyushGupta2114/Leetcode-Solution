import numpy
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(0,len(matrix)):
            for j in range(i,len(matrix[i])):
                if(i!=j):
                    print(matrix[i][j],matrix[j][i])
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

#         matrixumpy.transpose(matrix))
        for i in matrix:
            i.reverse()
        return matrix
