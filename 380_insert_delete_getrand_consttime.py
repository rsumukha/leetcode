import random
class RandomizedSet(object):

    def __init__(self):
        self.mydict = {}
        self.arr = []        
        

    def insert(self, val):

        if val in self.mydict:
            return False
        length = len(self.arr)
        self.mydict[val] = length
        self.arr.append(val)
        return True
        
        

    def remove(self, val):
        if not val in self.mydict:
            return False
        self.mydict[self.arr[len(self.arr)-1]] = self.mydict.get(val)
        self.arr[len(self.arr)-1], self.arr[self.mydict.get(val)] = self.arr[self.mydict.get(val)], self.arr[len(self.arr)-1]
        del self.arr[len(self.arr)-1]
        del self.mydict[val]
        return True
        
        

    def getRandom(self):
        r = random.randint(0, len(self.arr)-1)
        return self.arr[r]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
