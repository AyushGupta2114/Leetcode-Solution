class Solution {
public:
    int fib(int n) {
        int dt[40];
        dt[0]=0;
        dt[1]=1;
        for(int i=2;i<=n;i++)
            dt[i]=dt[i-1]+dt[i-2];
        return dt[n];
    }
};