class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        a=[]
        for i in range(0,len(matrix[0])):
            b=[]
            for j in range(0,len(matrix)):
                print(j)
                b.append(matrix[j][i])
            a.append(b)
        return a
       
       
       
       
    #    wrong
        # for i in range(0,len(matrix)):
        #     for j in range(0,len(matrix[i])-1):
        #         matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        # return matrix
        