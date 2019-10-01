# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.itera(root, p, q)
        
    def rec(self, root, p, q):
        if root==None:
            return None
        if p.val < root.val and q.val < root.val:   ##HINT: COMPARE P AND Q VALUE WITH ROOTVALUE NOT THE OTHER WAY ROUND
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:            
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        
    def itera(self, root, p, q):
        if root==None:return None
        stack=[]
        stack.append(root)
        while stack:
            cur=stack.pop()
            if p.val > cur.val and q.val > cur.val:
                stack.append(cur.right)
                continue
            elif p.val < cur.val and q.val < cur.val:
                stack.append(cur.left)
                continue
            else:
                return cur
        return
