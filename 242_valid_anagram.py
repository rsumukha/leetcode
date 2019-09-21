class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        
        if len(s)==0 or len(t)==0:
            return True
        
        d={}
        for i in range(len(s)):
            if d.get(s[i], -1)==-1:
                d[s[i]]=1
            else:
                d[s[i]]+=1
        print(d)
        for i in range(len(t)):
            if d.get(t[i], -1)==-1:
                return False
            else:
                d[t[i]]-=1
        print(d)
        
        for i in d.keys():
            if d[i]!=0:
                return False
        
        return True
        