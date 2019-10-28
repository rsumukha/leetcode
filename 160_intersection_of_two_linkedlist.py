# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        if headA == None or headB == None:
            return None
        
        def cnt(temp):
            count=0
            while temp!= None:
                temp = temp.next
                count += 1
            return count
        
        temp = headA
        counta = cnt(temp)
        temp = headB
        countb = cnt(temp)
        if counta == countb:
            temp = headA
            temp2 = headB
        elif counta != countb:
            if counta > countb:
                temp = headA
                temp2 = headB
            else:
                temp= headB
                temp2 = headA
            x=abs(counta - countb)
            while x:
                x-=1
                temp = temp.next
        while temp!=None and temp2!=None and temp!=temp2:
            temp = temp.next
            temp2= temp2.next
        
        return None if (temp==None or temp2==None) else temp
        
        
