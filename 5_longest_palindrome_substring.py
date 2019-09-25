class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0 or len(s)==1:
            return s
        
        dp_array=[[0 for _ in range(len(s))] for _ in range(len(s))]
        
        for i in range(len(s)):
            dp_array[i][i]=1
            
        maxlen=1
        startindex=0
        endindex=0
        for width in range(1, len(s)):
            i=0
            j=i+width
            while i<len(s) and j<len(s):
            
                if (width==1 or dp_array[i+1][j-1]) and  s[i] == s[j]:
                    dp_array[i][j] = 1   
                    if (j - i +1) > maxlen:
                        maxlen = j - i +1
                        startindex=i
                        endindex = j
                else:
                    dp_array[i][j]=0

                i+=1
                j=i+width
                
        return s[startindex: endindex+1]
                