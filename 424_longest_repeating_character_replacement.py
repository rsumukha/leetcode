from collections import Counter
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ##sliding window technique
    
        if len(s)==0:
            return 0
        mydict=Counter()        
        max_length=0
        startptr=0
        for endptr in range(len(s)):
            mydict[s[endptr]]+=1            
            max_char_count=mydict.most_common(1)[0][1]
            while (endptr-startptr+1 - max_char_count > k ):
                mydict[s[startptr]]-=1
                startptr+=1            
            max_length = max(max_length, endptr-startptr+1)           
            
        return max_length