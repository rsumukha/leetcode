class ListNode(object):
    def __init__(self, v):
        self.val=v
        self.next=None


class Solution:
    def mergeTwoLists(self, l1,l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val>=l2.val:
            l2.next=self.mergeTwoLists(l1, l2.next)
            return l2
        else:
            l1.next=self.mergeTwoLists(l1.next, l2)
            return  l1

def printll(r):
    while (r != None):
        print(str(r.val))
        r = r.next


if __name__=="__main__":
    a=ListNode(1)
    a.next=ListNode(3)
    a.next.next=ListNode(6)
    b=ListNode(-9)
    # b.next=ListNode(0)
    # b.next.next=ListNode(3)
    s=Solution()
    # printll(a)
    # printll(b)
    r=s.mergeTwoLists(a,b)
    print("Ans")
    printll(r)

        

##iterative solution

        # dummyNode=ListNode(0)
        # retNode=dummyNode
        
        # while l1!=None and l2!=None:
        #     # print(dummyNode.val)
        #     if l1.val<=l2.val:
        #         dummyNode.next=l1
        #         l1=l1.next
        #     else:
        #         dummyNode.next=l2
        #         l2=l2.next
        #     dummyNode=dummyNode.next
        # if l1==None:
        #     dummyNode.next=l2
        # if l2==None:
        #     dummyNode.next=l1
        # return retNode.next