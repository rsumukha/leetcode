"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return None
        
        #without dictionary
        tmp = head
        while tmp != None:
            newnode = Node(tmp.val, tmp.next, None)
            tmp.next = newnode
            tmp = newnode.next
        
        tmp = head
        newhead = tmp.next
        while tmp != None:
            # print("a")
            cpytmp = tmp.next
            if tmp.random != None:
                cpytmp.random = tmp.random.next
            else:
                cpytmp.random = None
            tmp = cpytmp.next
        
        tmp = head
        while tmp!=None:
            cpytmp = tmp.next
            tmp.next = cpytmp.next
            tmp = cpytmp.next
            if tmp == None:
                cpytmp.next = None
            else:
                cpytmp.next = tmp.next
        
        return newhead
            
        
        
