class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    ret_list=[]
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.ret_list = []
        arr = []

        self.recSum(root, sum, arr)
        return self.ret_list

    def recSum(self, root, s, arr):
        arr.append(root.val)

        if root.right == None and root.left == None:
            if sum(arr) == s:
                self.ret_list.append(arr)
            else:
                return

        if root.left:
            self.recSum(root.left, s, arr.copy())
        if root.right:
            self.recSum(root.right, s, arr.copy())

if __name__=='__main__':
    s=Solution()
    root=TreeNode(5)
    root.left=TreeNode(4)
    root.right=TreeNode(8)
    root.right.left=TreeNode(13)
    root.right.right=TreeNode(4)
    root.right.right.left=TreeNode(5)
    root.right.right.right=TreeNode(1)
    root.left.left=TreeNode(11)
    root.left.left.left=TreeNode(7)
    root.left.left.right=TreeNode(2)

    print(s.pathSum(root, 22))
