# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        return self.iterative(root, k)
        # self.kthsmallest = 0
        # self.k=k
        # self.kthSmallest_helper(root)
        # return self.kthsmallest
    
    def kthSmallest_helper(self, root):
        if root==None:
            return      
        self.kthSmallest_helper(root.left)
        self.k-=1
        if self.k==0:
            self.kthsmallest = root.val
            return
        self.kthSmallest_helper(root.right)
        return
    
    def iterative(self, root, k):
        stack =[]
        stack.append(root)
        cur=root
        while cur!=None or stack:
            while cur!=None:
                stack.append(cur)
                cur=cur.left
            cur = stack.pop()
            k-=1
            if k==0:
                return cur.val
            cur=cur.right
        return 
            
