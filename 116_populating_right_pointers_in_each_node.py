"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None:
            return None
        root.next= None
        queue = collections.deque()
        queue.append(root)
        queue.append(None)
        
        while queue:
            current = queue.popleft()
            if current:
                current.next = queue[0]
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            elif queue:
                queue.append(None)
        return root
            
        
