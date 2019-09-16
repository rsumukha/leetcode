# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #1pass
        dummyNode=ListNode(0)
        retNode=dummyNode
        dummyNode.next=head
        fptr=dummyNode
        for _ in range(n+1):
            fptr=fptr.next
            
        while fptr!=None:
            fptr=fptr.next
            dummyNode=dummyNode.next
        dummyNode.next=dummyNode.next.next
          
        
        return retNode.next
        # 2pass
        dummyNode=ListNode(0)
        retNode=dummyNode
        dummyNode.next=head
        leng=0
        while head!=None:
            leng+=1
            head=head.next
            
        for _ in range(leng-n):
            dummyNode=dummyNode.next
        dummyNode.next=dummyNode.next.next
        
        return retNode.next
        