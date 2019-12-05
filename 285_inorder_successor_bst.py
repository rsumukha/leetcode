# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        self.found = False
        self.res = None
        
        def inorder(root):
            if root == None:
                return 
            
            
            if root.val > p.val:
                inorder(root.left)
            if self.found:
                if not self.res:
                    self.res = root
                    return
            if root == p:
                self.found = True
        
            inorder(root.right)
            return 
        
        
        inorder(root)
        return self.res
         
        
        
