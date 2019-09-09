class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        dp = [[0 for i in range(len(text2)+1) ] for j in range(len(text1)+1)]
        print(dp)

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i]==text2[j]:
                    dp[i+1][j+1]=dp[i][j]+1
                else:
                    dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])        
        print(dp)
        return dp[-1][-1] 

        ## this doesnt work and the below one works because  * creates the copy with reference
        ##so use for

    def longestCommonSubsequence1(self, text1, text2):

        n,m=len(text1),len(text2)

        dp=[[0]*(m+1) for _ in range(n+1)]

        for i in range(n):
            for j in range(m):
                if text1[i]==text2[j]:
                    dp[i+1][j+1]=dp[i][j]+1
                else:
                    dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
        print(dp)
        return dp[-1][-1]



        ## if equal check up untill now excluding the char whats the lcs and +1
        ## else check whats maximim, including i  and excluding j or vv





if __name__=="__main__":
    s=Solution()
    print(s.longestCommonSubsequence("abcde" ,"ace"))

    print(s.longestCommonSubsequence1("abcde", "ace"))
