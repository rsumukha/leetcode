class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 2:
            return True
        
        leftptr = 0 
        rightptr = len(s)-1
        candelete = True
        while leftptr<rightptr:
            if s[leftptr] != s[rightptr]:
                
                def vPalindrome(string):
                    # print(string)
                    if len(string)==1:
                        return True
                    lptr= 0
                    rptr = len(string)-1
                    while lptr<rptr:
                        if string[lptr]!=string[rptr]:
                            return False
                        lptr+=1
                        rptr-=1
                    return True
                
                return vPalindrome(s[leftptr+1:rightptr+1]) or vPalindrome(s[leftptr:rightptr])
            else:
                leftptr+=1
                rightptr-=1
        return True
