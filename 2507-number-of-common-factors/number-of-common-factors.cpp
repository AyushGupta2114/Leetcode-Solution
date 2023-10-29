class Solution {
public:

    vector<int>vetdivisor(int num)
    {
        vector<int>k;
        for(int i=1;i*i<=num;i++)
        {
            if(num%i==0)
            {
                k.push_back(i);
                if(i!=num/i)
                {
                    k.push_back(num/i);
                }
            }
        }
        return k;
    }

    int commonFactors(int a, int b) {
        vector<int>k=vetdivisor(b);
         for (int l : k) {
        std::cout << l << " ";
    }
    cout<<endl;
    vector<int>z=vetdivisor(a);
        for (int j : z)
        {
        cout << j << " ";
        }
    int commanCount=0;
    for (int element1 : k) {
        for (int element2 : z) {
            if (element1 == element2) {
                commanCount++;
                break;  // Exit the inner loop once a common element is found
            }
        }
    }
    return commanCount;
    // std::cout << "Number of common elements: " << commanCount << std::endl;
    //     int f=0;
    // return f;
    }
    
};