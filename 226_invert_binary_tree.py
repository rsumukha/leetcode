# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
  
        if root==None:
            return None
        
        return self.bfs(root)
    
    def stackdfs(self, root):
        if root==None:
            return None
        
        root.right, root.left = root.left, root.right
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    def bfs(self, root):
        queue=collections.deque()
        queue.append(root)
        
        while queue:
            current = queue.popleft()
            
            current.left, current.right = current.right, current.left
            
            if current.left!=None:
                queue.append(current.left)
            if current.right!=None:
                queue.append(current.right)
    
        return root
    
    ##CANT DO IT LIKE THIS, WONT WORK
    def invert(self, lroot, rroot): 
        if lroot==None and rroot==None:
            return 
        if lroot==None:
            rroot.val = lroot
            return 
        if rroot==None:
            lroot.val = rroot
            return None
        else:
            lroot.val, rroot.val = rroot.val, lroot.val
        self.invert(lroot.left, rroot.right)
        self.invert(lroot.right, rroot.left)
        
        
        