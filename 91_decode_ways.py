class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if int(s)<=0:
            return 0
        if int(s[0])==0:
            return 0
        dp_array=[0 for i in range(len(s)+1)]
        dp_array[0]=1
        dp_array[1]=1

        for i in range(1, len(s)):
            one=int(s[i])
            two=int(s[i-1]+s[i])
            
            if one>0:
                dp_array[i+1] += dp_array[i]
            if two>=10 and two<=26:
                dp_array[i+1] += dp_array[i-1]
        print(dp_array)
                
        return dp_array[len(s)]
            
            



        print(dp_array)
        return dp_array[len(s)]

if __name__=="__main__":
    s=Solution()
    print(s.numDecodings("226"))
