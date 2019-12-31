# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
 
        def reverse(head, prev, c):
            tmp = head
            cur = head
            while head != c:
                head = head.next
                cur.next = prev
                prev = cur
                cur = head
            return prev, tmp
        
        def p(a):
            while a!= None:
                print(a.val)
                a=a.next
            print(" ")
        
        left = None
        khead = head
        first = True
        returnnode = head
        cnt = 0
        
        while head != None:   
            print(head)
            if cnt == k-1 :                
                kleft, kright = reverse(khead, left, head.next)
                if first:
                    returnnode = kleft
                    first = False
                else:
                    left.next = kleft
                left = kright
                kright.next = head.next
                khead = head.next
                cnt = 0
                # print("complete")
                # p(returnnode)
                # print("left")
                # print(left.val)
                # print("khead - kleft - kright")
                # print(khead.val, kleft.val, kright.val)
                continue
                
            cnt += 1
            head = head.next
        
        return returnnode
            
        
            
                
            
            
            
            
            
        
