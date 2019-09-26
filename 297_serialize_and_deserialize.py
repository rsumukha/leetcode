# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if root==None:
            return ""
        
        queue=collections.deque()
        queue.append(root)
        out=[]
        while queue:
            current = queue.popleft()
            if current==None:
                out.append("null")
                continue
            else:
                out.append(str(current.val))           
            
            if current.left==None:
                queue.append(None)
            else:
                queue.append(current.left)
                
            if current.right==None:
                queue.append(None)
            else:
                queue.append(current.right)
                
        for i in range(len(out)-1 , -1, -1):
            if out[i]!="null":
                break
        # print(str(out[:i+1]))
        return ",".join(out[:i+1])
        
    ##use preorder traversal

    def deserialize(self, data):
        if len(data)==0:
            return None
        ar=data.split(',')
        return self.recursive(ar, 0)
    
    def recursive(self, data, idx):
        if idx>=len(data):
            return None
        root=TreeNode(data[idx])
        root.left = self.recursive(data, 2*idx+1)
        root.right = self.recursive(data, 2*idx+2)
        return root


            
        
        
