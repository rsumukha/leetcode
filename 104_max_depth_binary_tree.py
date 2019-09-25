# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.max3(root)
        
    def max(self, root):
        if root==None:
            return 0
        l=self.max(root.left)
        r=self.max(root.right)
        if l>r:
            return l+1
        else:
            return r+1
    
    def max2(self, root):
        if root==None:
            return 0
        l=1+self.max2(root.left)
        r=1+self.max2(root.right)
        if l<r:
            return r
        else:
            return l
    
    def max3(self, root):
        if root==None:
            return 0
        l= 0 if root.left==None else self.max3(root.left)
        r= 0 if root.right==None else self.max3(root.right)
        
        return 1+max(l,r)
        