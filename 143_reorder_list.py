# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head==None or head.next==None:
            return head
        a, b =self.splitList(head)
        self.printll(a)
        self.printll(b)
        b=self.rev(b)
        self.printll(b)
        c=self.merge(a, b)
        self.printll(c)
        return head
        
    def merge(self, a, b):
        ret=a
        while a!=None and b!=None:
            tmp=a.next
            a.next=b
            b=b.next
            a.next.next=tmp
            a=tmp
        return ret
    
    
    def splitList(self, n):
        fptr=n
        sptr=n
        
        while fptr!=None and fptr.next!=None:
            fptr=fptr.next.next
            sptr=sptr.next
        retptr=sptr.next
        sptr.next=None
                
        return n, retptr
    

    def rev(self, head):
        cur=head
        prev=None
        while head!=None:
            head=head.next
            cur.next=prev
            prev=cur
            cur=head
        return prev
    
    def printll(self, node):
        while node!=None:
            print(node.val)
            node=node.next