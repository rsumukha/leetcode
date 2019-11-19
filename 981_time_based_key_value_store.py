"""
TP: using bisect for binary search ** bisect is powerful and important
bisect usage:
import bisect

**bisect.bisect_left(a, x, lo=0, hi=len(a)) returns the position of x in list a.**

similarly bisect_right

"""
import bisect
from collections import defaultdict, OrderedDict
class TimeMap(object):

    def __init__(self):
        self.keyval = defaultdict(list)
        self.keytime = defaultdict(list)
        
        

    def set(self, key, value, timestamp):
        self.keyval[key].append(value)
        self.keytime[key].append(timestamp)
                
        

    def get(self, key, timestamp):
        array=self.keytime[key]
        k= bisect.bisect(array, timestamp)
        return "" if k == 0 else self.keyval[key][k-1]

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
