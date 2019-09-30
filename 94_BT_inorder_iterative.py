# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.l =[]
        self.itera(root)
        return self.l
    
    def rec(self, root):
        if root ==None:
            return None
        self.rec(root.left)
        self.l.append(root.val)
        self.rec(root.right)
        return
    
    def itera(self, root):
        if root==None:
            return
        stack =[]
        cur=root
        while cur!=None or stack:
            while cur!=None:
                stack.append(cur)
                cur=cur.left
            cur = stack.pop()
            self.l.append(cur.val)
            cur=cur.right
        return
        
