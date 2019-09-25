# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        dictionary={}
        return self.findsum2(root, k, dictionary)
        
    #logn hashtable method
    def findsum(self, root, k, dictionary):
        if root==None:
            return False
        if dictionary.get(root.val, None)!=None:
            return True
        else:
            dictionary[k-root.val]=True
            
        return self.findsum(root.left, k,dictionary) or self.findsum(root.right, k,dictionary)
    
    