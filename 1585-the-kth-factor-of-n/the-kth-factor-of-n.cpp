class Solution {
public:
    int kthFactor(int n, int k){
        if(n==1 and k==1){
            return 1;
        }
        vector <int>a;
            int i;
            for(i=1;i*i<n;i++)
            {
                if(n%i==0)
                {
                a.push_back(i);
                }
            }
            for(;i>=1;i--)
            {
                if(n%i==0)
                {
                    // cout<<n/i;
                    int k=0;
                    if(a.back()==n/i and k==0)
                    {
                        k=1;
                    }
                    else
                    {
                        a.push_back(n/i);
                    }
                }
            }
    
    if (k >= 0 && k <= a.size()) {
        int nthElement = a[k-1];
        return nthElement;
    } else {
        return -1;
    }
    return 0;
    }
};