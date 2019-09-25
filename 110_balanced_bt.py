# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if self.balance(root)==-1:
            return False
        else:
            return True
        
    def balance(self, root):
        if root==None:
            return 0
        l=self.balance(root.left)
        r=self.balance(root.right)
        print(l, r, root.val)
        if abs(l-r)>1 or l==-1 or r==-1:
            return -1
        else:
            return max(l,r) +1
        