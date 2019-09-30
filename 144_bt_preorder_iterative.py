# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None:
            return None
        self.list_=[]
        self.iterative(root)
        return self.list_
    
    def iterative(self, root):
        stack =[]
        stack.append(root)
        while stack:
            current = stack.pop()
            self.list_.append(current.val)
            if current.right !=None:
                stack.append(current.right)
            if current.left!=None:
                stack.append(current.left)
        return
