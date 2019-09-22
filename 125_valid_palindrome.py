class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==0:
            return True
        
        leftptr=0
        rightptr=len(s)-1
        
        
        while leftptr<rightptr:
            while leftptr<rightptr and not s[leftptr].isalnum():
                leftptr+=1
            while leftptr<rightptr and not s[rightptr].isalnum():
                rightptr-=1
            if s[leftptr].lower()!= s[rightptr].lower():
                return False
            leftptr+=1
            rightptr-=1
        return True