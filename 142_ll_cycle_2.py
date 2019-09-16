# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        mydict={}
        count=1
        
        while head!=None:
            if mydict.get(head, 0)!=0:
                return mydict[head]
            else:
                mydict[head]=head
            count+=1
            head=head.next
        return None