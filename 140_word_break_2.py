class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        
        wordset = set(wordDict)
        cache = {}
        res =[]
        
        def dfs(word, cur):
            
            if word in cache:
                for item in cache[word]:
                    res.append(cur+item)
                return
            
            if word in wordset:
                ans=cur+word
                res.append(ans)     
                
            for i in range(1, len(word)):
                first = word[:i]
                second = word[i:]                
                if first in wordset:
                    dfs(second, cur+first + " ")
            
            cache[word] = res[:]            
            return cache[word]
            
        return dfs(s, "")

