# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    summ=0
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if(root):
            if root.left and not root.left.left and not root.left.right:
                self.summ+=root.left.val
            self.sumOfLeftLeaves(root.left)
            self.sumOfLeftLeaves(root.right)
        return self.summ

        