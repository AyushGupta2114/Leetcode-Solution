class Solution {
public:
    int pivotInteger(int n) {
        int s1=0,s2=0,pivot=0;
        for(int i=1;i<=n;i++)
        {
            s1+=i;
            for(int j=i;j<=n;j++){
                s2+=j;
            }
            if(s1==s2){
            pivot=i;
            break;
            }
            s2=0;
        }
        if(pivot==0)
        return -1;
        else
        return pivot;
    }
};