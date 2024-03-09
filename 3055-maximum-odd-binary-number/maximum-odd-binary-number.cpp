class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        sort(s.rbegin(),s.rend());
        // cout>>s;
        if(s[0]=='1'){
          s.erase(0,1);
          s +='1';  
        }
        return s;
    }
};