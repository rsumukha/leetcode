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
        self.recursiveSol(head)

    def nonrecursiveSol(self, head):
        temph=head
        temp=None
        while head!=None:
            head=head.next
            temph.next=temp
            temp=temph
            temph=head
        return temp


    def rec(self, head):
        if head==None or head.next==None:
            return head
        p= self.rec(head.next)
        head.next.next=head
        head.next=None
        return p

    def rec(self, head):
        if head.next.next==None:
            head.next.next=head
            return head
        else:
            head=self.rec(head.next)
        return head

        


if __name__=="__main__":
    s=Solution()
    print(s.reverseList())