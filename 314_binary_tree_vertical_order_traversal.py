# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        dictionary = {}
        
        def levelorder(root, colnum):
            from collections import deque
            queue = deque()
            queue.append((root,colnum))            
            while queue:
                current, colnum = queue.popleft()
                if current != None:
                    if colnum in dictionary:
                        dictionary[colnum].append(current.val)
                    else:
                        dictionary[colnum] = [current.val]
                    if current.left:
                        queue.append((current.left, colnum+1))
                    if current.right:
                        queue.append((current.right, colnum-1))
            return
            
        levelorder(root, 0)
        results = []
        [results.append(dictionary[x]) for x in sorted(dictionary.keys(), key = lambda x: -x)]
        return results
        
