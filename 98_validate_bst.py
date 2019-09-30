# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        return self.sol(root, float('-inf'), float('inf'))
    
    def sol(self, root, low, high):
        if root==None:return True
        if root.val>=high or root.val<=low:return False
        
        return self.sol(root.left, low, root.val) and self.sol(root.right, root.val, high)
        
        
        
    def solution_that_doest_work(self): ###it checks only if left<root>right satisfying the local,[10,5,15,null,null,6,20]
        if root==None:
            return True
        
        flagl = self.isValidBST(root.left) 
        flagr = self.isValidBST(root.right)
        if flagl and flagr:
            if root.left!=None and root.right!=None:
                if root.val>root.left.val and root.val<root.right.val:
                    return True
            elif root.left==None and root.right==None:
                return True
            elif root.left==None and root.val<root.right.val:
                return True
            elif root.right==None and root.val>root.left.val:
                return True
        return False
        

        
