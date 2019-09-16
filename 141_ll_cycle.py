# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        myset=set()
        
        while head!=None:
            if head in myset:
                return True
            else:
                myset.add(head)
            head=head.next
            
        return False
        
        ####
        #fast ptr impl
        
        if head ==None or head.next==None or head.next.next==None:
            return False
        if head.next==head:
            return True
        fptr=head.next
        sptr=head
        
        while fptr.next!=None and fptr.next.next!=None:
            if fptr==sptr:
                return True
            fptr=fptr.next.next
            sptr=sptr.next
        return False
    
    #or check the hashtable and store all the pointers
        