class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        X=x
        y=0
        while(x>0):
            rem=x%10
            y =rem+ y*10
            #print(y)
            x=int(x/10)
        if y==X:
            return True
        else:
            return False

if __name__=="__main__":
    s=Solution()
    print(s.isPalindrome(111))