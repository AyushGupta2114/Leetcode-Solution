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
    long ans=0;
    int sumNumbers(TreeNode* root) {
        if(root==NULL)
            return 0;
        preorder(root,0);
        return ans;
    }
    void preorder(TreeNode *root,long val)
    {
        if(root==NULL)
        return;
        if(root!=NULL)
        {
            val*=10;
            val+=root->val;
            cout<<val<<endl;
             if(root->left==NULL && root->right==NULL)
            {
                ans+=val;
                return;
            }
        preorder(root->left,val);
        preorder(root->right,val);
        }
        

    }
};