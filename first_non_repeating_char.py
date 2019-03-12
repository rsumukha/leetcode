class Solution(object):
    def nonrepeating(self, str):
        count=[0]*500
        for i in str:
            if count[ord(i)]:
                count[ord(i)]+=1
            else:
                count[ord(i)]=1
        for j in str:
            if count[ord(j)]==1:
                return chr(ord(j))



if __name__ == "__main__":
    s = Solution()
    print(s.nonrepeating("aaacccb"))