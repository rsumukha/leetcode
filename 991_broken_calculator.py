class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        
        return self.recursion(X,Y)
        
    def recursion(self, X, Y):
        if X==Y:
            return 0
        if X>Y:
            return X-Y
        if Y%2 == 0:
            return self.recursion(X, int(Y/2)) + 1
        elif Y%2 ==1:
            return self.recursion(X, Y+1) + 1
        
        
