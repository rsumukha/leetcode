# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        
        if root == None:
            return None
        
        self.retarray = []
        
        self.retarray.append(root.val)
        
        def leftboundary(root):
            if not root or root.left == None and root.right== None:
                return 
            self.retarray.append(root.val)

            if root.left:
                leftboundary(root.left)
            else:
                leftboundary(root.right)

        def leaf(root):
            if root==None:
                return 
            if root.left == None and root.right == None:
                self.retarray.append(root.val)
            leaf(root.left)
            leaf(root.right)
            
        def rightboundary(root):
            if not root or root.left == None and root.right== None:
                return 
            if root.right:
                rightboundary(root.right)
            else:
                rightboundary(root.left)
            self.retarray.append(root.val)   #postorder
        
        leftboundary(root.left)
        leaf(root.left)
        leaf(root.right)
        rightboundary(root.right)
        
        return self.retarray

