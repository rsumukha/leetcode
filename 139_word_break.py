class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
         wordset = set(wordDict)
        visited=set()

        def dfs(word):
            if word in visited:
                return False
            if word in wordset:
                return True

            for i in range(1, len(word)):
                first = word[:i]
                second = word[i:]

                if first in wordset:
                    if second in wordset:
                        return True
                    if dfs(second):
                        return True
            visited.add(word)
            return False

        return dfs(s)
              
        dp_array=[0]*(len(s)+1)
        dp_array[0]=1
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                print(s[i:j+1])
                if dp_array[i] and s[i:j+1] in wordDict:
                    dp_array[j+1]=1
                    
            print(dp_array)
        
        if dp_array[len(s)]==1:
            return True
        else:
            return False



if __name__=="__main__":
    s=Solution()
    print(s.wordBreak("aaaaaaa", ["aaaa","aaa"]))
    #"aaaaaaa"
    # print(s.wordBreak("leetcode", ["leet","code"]))

