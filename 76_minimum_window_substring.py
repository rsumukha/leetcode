from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        #sliding window
        if len(t)>len(s):
            return ""
        countdict=Counter(t)
        total_t_chars=len(countdict.keys())
        
        leftptr=0
        minleft=float("-inf")
        minright=float("inf")
        
        current_length=0
        found=False
        for rightptr in range(0, len(s)):
            
            # move rightptr till we get all results and condition is satisfied 
            if countdict.get(s[rightptr], None)!=None:
                countdict[s[rightptr]]-=1
                if countdict.get(s[rightptr])==0:
                    current_length+=1
            
            #move leftptr till the condition is satisfied and add value to dict
            while leftptr<=rightptr and current_length==total_t_chars:
                
                if min(minright-minleft, rightptr-leftptr) == (rightptr-leftptr):
                    found=True
                    minleft, minright = leftptr, rightptr            

                if countdict.get(s[leftptr], -1)==0:
                    current_length-=1
                    countdict[s[leftptr]]+=1
                elif countdict.get(s[leftptr], float("inf"))<0:
                        countdict[s[leftptr]]+=1
                
                leftptr+=1
        if found:
            return s[minleft:minright+1]
        else:
            return ""
                    
                    
                    
                
            
        