# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        queue=[]
        
        for li in lists:
            if li!=None:
                heapq.heappush(queue, (li.val, li) )
                
        dummyNode=ListNode(0)
        retNode=dummyNode
        
        while queue:
            val, cur=heapq.heappop(queue)
            dummyNode.next=cur
            if cur.next!=None:
                heapq.heappush(queue, (cur.next.val, cur.next))
            dummyNode=dummyNode.next
                      
        return retNode.next
        
        
        
                
                
            
        
        
        