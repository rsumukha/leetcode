# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        return self.minD(root)
        # if root==None:
        #     return 0
        # l=self.minD(root.left)
        # r=self.minD(root.right)
        # if l==0 or r==0:
        #     return l+r+1
        # else:
        #     return min(l,r)+1

    def minD(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        l=self.minD(root.left)
        r=self.minD(root.right)
        if l==0 or r==0:
            return l+r+1
        return min(l,r)+1
        