class LRUCache(object):

    def __init__(self, capacity):
        self.cachequeue = collections.deque()
        self.mydict = {}
        self.maxcapacity = capacity
        

    def get(self, key):
        if self.mydict.get(key, None):
            self.cachequeue.remove(key) # expensive if we are 
            self.cachequeue.append(key)            
            return self.mydict[key]
        else:
            return -1
        

    def put(self, key, value):
        if self.mydict.get(key, None):
            self.mydict.pop(key, None)    
            self.cachequeue.remove(key)
        self.mydict[key] = value
        self.cachequeue.append(key)
        if len(self.cachequeue) > self.maxcapacity:
            keytopop = self.cachequeue.popleft()
            self.mydict.pop(keytopop, None)
        return
            
        

