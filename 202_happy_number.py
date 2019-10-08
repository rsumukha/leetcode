class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True
        visited = set()
        visited.add(n)
        while n:
            newnumber=0
            for i in str(n):
                newnumber += int(i)**2
            if newnumber in visited:
                return False
            visited.add(newnumber)
            if newnumber == 1:
                return True
        
            n=newnumber
        
