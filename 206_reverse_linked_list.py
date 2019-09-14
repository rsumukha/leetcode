# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        self.nonrecursiveSol(head)
        self.recursiveSol(temp)



    def nonrecursiveSol(self, head):
    	temp=head


    	while temp.next!=None:
    		head=head.next


    		temp=temp.next


    def recursiveSol(self, head):

        






if __name__=="__main__":
	s=Solution()
	print(s.reverseList())