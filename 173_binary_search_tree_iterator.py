# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):   #We can use generators in python
        self.stack = []         #use stack to store all the left node values
        self.puttostack(root)
        
    def puttostack(self, root):
        while root:                     #put every left value to stack
            self.stack.append(root)
            root = root.left

    def next(self):
        cur = self.stack.pop()          #when popping a node if it has a right then put all its left value
        if cur.right:
            self.puttostack(cur.right)  #stack will always take less than O(h) space 
        return cur.val
        

    def hasNext(self):
        return True if len(self.stack) else False
        

