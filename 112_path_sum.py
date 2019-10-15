# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        if root == None:
            return False
        if sum-root.val==0 and root.right==None and root.left==None:
            return True
        
        leftsum = self.hasPathSum(root.left, sum-root.val)
        rightsum = self.hasPathSum(root.right, sum-root.val)
        if leftsum or rightsum:
            return True
        else:
            return False
        
