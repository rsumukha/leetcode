
class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
class LRUCache(object):

    def __init__(self, capacity):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}
        self.maxcapacity = capacity
        self.currentqueuelength = 0
 
    
    def get(self, key):
        if key in self.cache:
            # node = self.cache[key]
            self.deletenode(self.cache[key])
            self.addnode(self.cache[key])
            return self.cache[key].value
        else:
            return -1
   

    def put(self, key, value):
        if key in self.cache:            
            self.deletenode(self.cache[key])
            del self.cache[key]
        self.cache[key] = Node(key,value)
        self.addnode(self.cache[key])
        if self.currentqueuelength > self.maxcapacity:
            del self.cache[self.tail.prev.key]
            self.deletenode(self.tail.prev)
        return 
    
    def addnode(self, node):
        tmpnode = self.head.next 
        self.head.next = node
        node.next = tmpnode
        node.prev = self.head
        tmpnode.prev = node
        self.currentqueuelength += 1
        
    
    def deletenode(self, nodetobedeleted):
        prev = nodetobedeleted.prev
        next = nodetobedeleted.next
        prev.next = next
        next.prev = prev
        self.currentqueuelength -= 1
            
    
            
            
        
            
        

