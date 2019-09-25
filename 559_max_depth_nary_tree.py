"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root==None:
            return 0
        if len(root.children)==0:
            return 1
        depth=0
        for child in root.children:
            depth = max(depth, self.maxDepth(child))
        return 1+depth
        