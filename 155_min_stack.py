"""
TP - get the minimum at each element, you dont have to recompute everytime you can cache it in,
* instead of thinking complicated DS think the basic things need to be done
1. We need minimum element O(1)
2. we need an algo to compute min when pushed and poped 

Think of the edge cases
"""
from collections import deque 
class MinStack(object):

    def __init__(self):
        self.stack = deque()
        self.minimum = float("inf")
        

    def push(self, x):
        self.minimum = min(self.minimum, x)
        self.stack.append((x, self.minimum))
        

    def pop(self):
        self.stack.pop()
        if len(self.stack)!=0:            
            _, self.minimum = self.stack[-1]
        else:
            self.minimum = float("inf")
        
        

    def top(self):
        return self.stack[-1][0]
        

    def getMin(self):
        return self.minimum
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
