class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if len(words) == 0 or len(words) == 1:
            return []
        wordset = set(words)
        output = []
        visited = set()
        
        
        def dfs(word):
            if word in visited:
                return True
                
            for i in range(1,len(word)):
                first = word[:i]
                second = word[i:]
                
                if first in wordset:
                    if second in wordset:
                        return True
                    if dfs(second):
                        return True
                    
            return False       
        
        
        for word in words:
            if dfs(word):
                output.append(word)
            visited.add(word)
        return output
        
        
