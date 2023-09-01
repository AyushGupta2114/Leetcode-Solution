class Solution {
public:
    bool searchMatrix(vector<vector<int>>& a, int target) {
        int m=a.size();
        int n=a[0].size();
        int i=0,j=n-1;
        while(i<m && j>=0)
        {
            if(a[i][j]==target)
                return 1;
            if(a[i][j]>target)
                j--;
            else if(a[i][j]<target)
                i++;
             
                   
        }
        return 0;
    }
};