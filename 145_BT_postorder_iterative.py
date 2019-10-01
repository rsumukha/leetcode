# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.l = []
        self.itera(root)
        self.l.reverse()
        return self.l
    
    def rec(self, root):
        if root == None:
            return None
        self.rec(root.left)
        self.rec(root.right)
        self.l.append(root.val)
        return
    
    def itera(self, root):
        if root ==None:
            return 
        stack =[]
        stack.append(root)
        while stack:
            cur = stack.pop()
            self.l.append(cur.val)
            if cur.left!=None:
                stack.append(cur.left)
            if cur.right!= None:
                stack.append(cur.right)
        return 
    
"""    
//inorder
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res=new ArrayList<>();
        if (root==null) return res;

        Stack<TreeNode> stack=new Stack<>();
        TreeNode curr=root;

        while(curr!=null || !stack.isEmpty()){
            while (curr!=null){
                stack.push(curr);
                curr=curr.left;
            }
            curr=stack.pop();
            res.add(curr.val);
            curr=curr.right;
        }
        return res;
    }

//preorder
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<>();
        if(root == null) return list;
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        while(!stack.isEmpty()) {
            TreeNode current = stack.pop();
            list.add(current.val);
            if(current.right!=null) {
               stack.push(current.right);
            }
            if(current.left!=null) {
              stack.push(current.left);
            }
        }
        return list;
    }

//postorder
      public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<>();
        if(root == null) return list;
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        while(!stack.isEmpty()) {
            TreeNode curr = stack.pop();
            list.add(0,curr.val);
            if(curr.left!=null) {
              stack.push(curr.left);
            }
            if(curr.right!=null) {
               stack.push(curr.right); 
            }
        }
        return list;
    }
"""
