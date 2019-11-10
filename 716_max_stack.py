"""
TP - use stack to store to provide push pop operation
second thought is to use heap to get the minimum element and store
but searching heap and deleting takes logn, can we search in constant time.
imporvisation- utilize hashmap with sorted order to know the minimum and deleting would be easier? - cant be done caus when the element is 
removed then the hashmap is not updated
"""

from collections import deque
import heapq
class MaxStack(object):

    def __init__(self):
        self.stack = []
        self.maximum = []
        self.idx = 0
        
        # self.stack = deque()
        # self.heap = []

    def push(self, x): #constant
        if len(self.maximum) == 0 or self.maximum[-1][0] <= x:
            self.maximum.append((x, self.idx))
        self.stack.append([x, self.maximum[-1]])
        self.idx += 1
    
        
        
        # heapq.heappush(self.heap, (-1)*x)
        # self.stack.appendleft(x)
        
    def pop(self): #constant
        if self.maximum[-1][0] == self.stack[-1][0]:
            self.maximum.pop()
        ret,_ = self.stack.pop()
        self.idx -= 1
        return ret
        
        
        # if len(self.stack) == 0:
        #     return
        # ret = self.stack.popleft()
        # self.heap.remove((-1)*ret)
        # heapq.heapify(self.heap)
        # return ret
        
    def top(self): #constant
        return self.stack[-1][0]
        
        # return self.stack[0]
        
    def peekMax(self): #constant
        return self.maximum[-1][0]
        
        
        # return (-1)*self.heap[0]
        
    def popMax(self): #N is worst case, amortized log(N)
        maxnum, idx = self.maximum.pop()
        del self.stack[idx]
        i = idx
        while i<len(self.stack):
            if len(self.maximum) == 0:
                self.maximum.append((self.stack[i][0], i))
            elif self.stack[i][0] >= self.peekMax():
                self.stack[i][1] = self.stack[i][0]
                self.maximum.append((self.stack[i][0], i))
            else:
                self.stack[i][1] = self.peekMax()
            i+=1
        self.idx -= 1
        return maxnum
        
        
        # ret = (-1)*self.heap[0]
        # self.stack.remove(ret)
        # heapq.heappop(self.heap)
        # return ret
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
