# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxsum=float("-inf")
        currentmax=float("-inf")
        x,y = self.maxpath(root, maxsum, currentmax)
        return x
    
    def maxpath(self, root, maxsum, currentmax):
        if root==None:
            return float("-inf"), float("-inf")
        
        ##improvement caus it wont send the root.left and root.right to rec (which is null anyway)
        if root.left==None and root.right==None:
            return root.val, root.val

        msum1, cm1 =self.maxpath(root.left, maxsum, currentmax)
        msum2, cm2 =self.maxpath(root.right, maxsum, currentmax)
        currentmax = max(cm1+root.val, cm2+root.val, root.val )
        maxsum =max(msum1, msum2,maxsum, currentmax, cm1+cm2+root.val, root.val)
        return maxsum, currentmax
    
