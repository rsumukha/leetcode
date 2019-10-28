#since the interval difference is 1, we can use the heapqueue to simulate treemap
# put everything in the heap then pop and merge if it is adjacent to each other
import heapq
class SummaryRanges(object):

    def __init__(self):
        self.intervals = []
        self.seen = set()   
        

    def addNum(self, val):
        if not val in self.seen:
            self.seen.add(val)
            heapq.heappush(self.intervals, [val,val])
            
        

    def getIntervals(self):
        mylist = []
        while self.intervals:
            current = heapq.heappop(self.intervals)
            if len(mylist) == 0:
                mylist.append(current)
            elif current[1] -1 == mylist[-1][1]:
                mylist[-1][1] = current[1]
            elif mylist[-1][1]+1 == current[0]:
                mylist[-1][1] = current[1]
            else:
                mylist.append(current)
        self.intervals = mylist
        return self.intervals
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
