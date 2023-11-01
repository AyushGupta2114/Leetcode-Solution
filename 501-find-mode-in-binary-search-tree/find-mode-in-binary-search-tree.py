# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        self.l=[]
        def inorder(root):
            if(root):
                self.l.append(root.val)
                inorder(root.left)
                inorder(root.right) 
        inorder(root)
        b=Counter(self.l)
        maxx=max(b.values())
        return [x for x in b if b[x]==maxx]
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        