# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # return self.build2(preorder, inorder, 0, len(inorder)-1, 0, len(inorder)-1)
        # return self.build(preorder, inorder)
        if len(preorder)==0:
            return None
        return self.iterative_dfs(preorder, inorder)
        
    def build(self, preorder, inorder):
        if len(preorder)==0:
            return None
        if len(inorder)==0:
            return None
        val=preorder.pop(0)
        root = TreeNode(val)
        idx = inorder.index(val)
        root.left = self.build(preorder,  inorder[:idx])
        root.right = self.build(preorder, inorder[idx+1:]  )
        return root
    
    def iterative_dfs(self, preorder, inorder):
        stack = []
        roott = TreeNode(preorder[0])
        stack.append((roott, preorder, inorder))
        
        while stack:
            args = stack.pop()
            root, preorder, inorder = args[0], args[1], args[2]
            if len(preorder)==0:
                continue            
            idx = inorder.index( root.val )
            
            if idx>0: ##left node exists
                root.left = TreeNode(preorder[1])
                stack.append(( root.left, preorder[1:idx+1], inorder[:idx] ))
            if idx<len(inorder)-1:
                root.right = TreeNode(preorder[idx+1])
                stack.append((root.right, preorder[idx+1:], inorder[idx+1:]))
        
        return roott

