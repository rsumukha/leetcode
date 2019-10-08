# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        #LEFT RIGHT ROOT / POSTORDER
        if not root:return None
        stack = []
        stack.append(root)
        while stack:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            if stack:
                current.right = stack[len(stack)-1]
            current.left = None
        
            
