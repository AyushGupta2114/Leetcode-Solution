class Solution {
public:
    int tribonacci(int n) {
        int dt[40];
        dt[0]=0;
      dt[1]=1;
       dt[2]=1;
        for(int i=3;i<=n;i++)
        {
            dt[i]=dt[i-1]+dt[i-2]+dt[i-3];
        }
        return dt[n];
    }
};