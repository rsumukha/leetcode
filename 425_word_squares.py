"""
Thought process:
Store all words into a trie. Iterate through the words.
For each word:
create a new list. Add the word into the list.
Search the trie for all the words that have the correct prefix. For each of these words:
Add it to the list.
Continue searching for the next prefix recursively.
The recursion reaches its base case when the size of the list is equal to the length of a word. In this case, we've found a word square.
"""


"""
finding prefix of a word is expensive ie n squared so we use prefix tree
"""

from collections import defaultdict
class TrieNode:
    def __init__(self, val):
        self.value = val
        self.wordend = False
        self.children = defaultdict(TrieNode)
    

class Solution:
    def buildTrie(self, words):
        self.root = TrieNode("*")
        for word in words:
            current = self.root
            for character in word:
                if not character in current.children.keys():
                    current.children[character] = TrieNode(character)
                current = current.children[character]
            current.wordend = True
    
    def printtree(self, root_):
        if root_.wordend:
            print(root_.value, end=" ")
        else:
            print(root_.value, end="")
        for node in root_.children.keys():               
            self.printtree(root_.children[node])
    
    def backtracking(self, seek, wordsquares):
        if seek == self.length:
            self.results.append(wordsquares)
            return
        
        prefix = "".join([word[seek] for word in wordsquares])        
        for prefixword in self.getallprefixwords(prefix):
            wordsquares.append(prefixword)
            self.backtracking(seek+1, wordsquares[:])
            wordsquares.pop()
    
    def getallprefixwords(self, prefix):
        re = []
        current = self.root 
        nodes = []
        for i,letter in enumerate(prefix):
            if not letter in current.children.keys():
                return re
            current = current.children[letter]
            
        def dfs(r, x):
            if r == None:
                return
            if r.wordend:
                re.append(prefix+"".join(x))
                return            
            for node in r.children.keys():
                x.append(node)
                dfs(r.children[node], x)
                x.pop()                  
                
        dfs(current, [])
        # print(re)
        return re        
        
        # re=[]
        # for word in self.words:
        #     if word.startswith(prefix):
        #         re.append(word)
        # return re        
    
    
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        self.words =words
        self.length = len(words[0])
        self.buildTrie(words)
        # self.printtree(self.root)
        self.results = []
        for word in words:
            wordsquares = [word]
            self.backtracking( 1, wordsquares)
        return self.results
            
            
        
