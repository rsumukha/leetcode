class Solution(object):
    def longestPalindrome(self, s):
        p=[[0 for i in range(len(s)) ] for j in range(len(s))]
        #print(len(s))
        for x in range(len(s)):
            #print(x)
            p[x][x]=1

        i=0
        j=1
        length_lps=1
        index=0
        while(i<(len(s)-1)):
            if s[i]==s[j]:
                p[i][j]=1
                length_lps=j+1
                index=i
            else:
                p[i][j]=0
            i+=1
            j+=1
        length=2

        while(length<=len(s)-1):
            #print(length)
            j=length
            i=0
            if length==7:
                pass
                #print(i, length)
            while(i<=(len(s)-1) and j<=len(s)-1):
                #print(p[i+1][j-1])

                if p[i+1][j-1]==1:

                    if s[i]==s[j]:
                        #print(s[i], s[j])
                        p[i][j]=1
                        index=i
                        length_lps=j+1
                    else:
                        p[i][j]=0
                else:
                    p[i][j]=0
                i+=1
                j+=1
            length+=1

        #print(length_lps)
        print(index)
        for i in range(len(s)):
            print(p[i])
        return s[index:length_lps]







if __name__ == "__main__":
    long_sub = Solution()
    print(long_sub.longestPalindrome("cbba"))