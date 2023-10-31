class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        vector<int>a;
        for(int i=0;i<nums.size();i++)
        {
        int count=0;
            for(int j=0;j<nums.size();j++)
            {
            if(nums[i]==nums[j])
            {
                count++;
            }
            }
            if(count%2!=0)
            {
                a.push_back(nums[i]);
                cout<<nums[i];
            }
        }
        return vector<int>{a[1],a[0]};
    }
};