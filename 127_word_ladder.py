class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        return self.singlebfs( beginWord, endWord, wordList)
        
    ##doesnt WORK, 
    """
    (u'hit', u'cog', 1, 1)
    (u'hot', u'cog', 2, 2)
    (u'dot', u'dog', 3, 2)
    (u'lot', u'log', 3, 2)
    (u'dog', u'dot', 4, 3)
    (u'log', u'lot', 4, 3)
    (u'cog', u'hot', 5, 4)
    """
    def bidibfs(self, beginWord, endWord, wordList):
        visitedf, visitedb =set(beginWord), set(endWord)
        wordList = set(wordList)
        queuef, queueb = collections.deque(), collections.deque()
        queuef.append((beginWord, 1))
        queueb.append((endWord, 1))
        while queuef and queueb:
            curfront, flen = queuef.popleft()
            curback, blen = queueb.popleft()
            print(curfront, curback, flen, blen)
            if curfront == curback:
                return flen+blen
            for i in range(len(curfront)):
                for character in string.ascii_lowercase:
                    newword = curfront[:i] +character + curfront[i+1:]
                    if newword not in visitedf and newword in wordList:
                        visitedf.add(newword)
                        queuef.append((newword, flen+1))
            
            for i in range(len(curback)):
                for character in string.ascii_lowercase:
                    newword = curback[:i] +character + curback[i+1:]
                    if newword not in visitedb and newword in wordList:
                        visitedb.add(newword)
                        queueb.append((newword, blen+1))
        return 0
        
        
    def singlebfs(self, beginWord, endWord, wordList):
        visited = set()
        wordList = set(wordList)
        queue = collections.deque()
        queue.append((beginWord,1))
        while queue:
            currentword, length = queue.popleft()
            if currentword ==endWord:
                return length
            for i in range(len(currentword)):
                for character in string.ascii_lowercase:
                    newword = currentword[:i] +character + currentword[i+1:]
                    if newword not in visited and newword in wordList:
                        visited.add(newword)
                        queue.append((newword, length+1))
        return 0
