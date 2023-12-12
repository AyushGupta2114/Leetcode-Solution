class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {
        int rows=matrix[0].size();
        int colums=matrix.size();

        std::vector<std::vector<int>>newMatrix(rows,std::vector<int>(colums,0));

        for(int i=0;i<rows;i++)
        {
            for(int j=0;j<colums;j++)
            {
                newMatrix[i][j]=matrix[j][i];
            }
        }
        return newMatrix;
        
    }
};