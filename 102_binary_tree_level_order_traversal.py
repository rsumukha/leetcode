# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return None
        return self.bfs(root)
        
    def bfs(self, root):
        queue=collections.deque()
        queue.append(root)
        queue.append('#')
        fout=[]
        out=[]
        while queue:
            current =queue.popleft()      
            if current=='#':
                if len(queue)==0:
                    fout.append(out)
                    return fout
                queue.append('#')
                fout.append(out)
                out=[]
                continue
            out.append(current.val)            
            if current.left!=None:
                queue.append(current.left)
            if current.right!=None:
                queue.append(current.right)        
        return fout
                
                
        