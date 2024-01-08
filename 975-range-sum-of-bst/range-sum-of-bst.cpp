#include <iostream>
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    public:
    int s=0;
    int rangeSumBST(TreeNode* root, int low, int high) {
        if(!root)
        {
            return 1;
        }
        cout<<root->val;
        if(root->val>=low && root->val<=high)
        {
            s=s+root->val;
        }
        rangeSumBST(root->left,low,high);

        rangeSumBST(root->right,low,high);
        return s;
    }
    
};