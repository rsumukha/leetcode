class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0 or len(s)==1:
            return len(s)
        
        dp_array = [[0 for _ in range(len(s))] for _ in range(len(s))]
        
        total=len(s)
        
        for i in range(len(s)):
            dp_array[i][i] = 1
        
        for width in range(1,len(s)):
            i=0
            j=width
            
            while i<len(s) and j<len(s):
                
                if (width==1 or dp_array[i+1][j-1]==1) and s[i] == s[j]:
                    dp_array[i][j] = 1
                    total+=1
                else:
                    dp_array[i][j] = 0
                
                i+=1
                j+=1
        return total