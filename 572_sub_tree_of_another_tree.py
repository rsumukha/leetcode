# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return self.rec(s, t, True)
        # return self.rec2(s, t)
    
    
    def rec2(self, s, t):
        if s==None:
            return False
        if s.val == t.val:
            if self.isST(s, t):
                return True    
        return self.rec2(s.left, t) or self.rec2(s.right, t)
    
    def isST(self, s, t):
        if s==None and t==None:
            return True
        if s==None or t==None:
            return False
        if s.val!=t.val:
            return False
        return self.isST(s.left, t.left) and self.isST(s.right, t.right)    
    
    
    def rec(self, s, t, head):
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False      
        if head:
            if s.val==t.val:
                if self.rec(s.right, t.right, False) and self.rec(s.left, t.left, False):
                    return True
        else:
            if s.val==t.val:
                if self.rec(s.right, t.right, False) and self.rec(s.left, t.left, False):
                    return True
            else:
                return False          
        return self.rec(s.right, t, True) or self.rec(s.left, t, True)
  

            

        

