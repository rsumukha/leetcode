class TrieNode():
    def __init__(self, char):
        self.val = char
        self.children = collections.defaultdict(TrieNode)
        self.end = False
    

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode("root")
        

    def addWord(self, word):
        cur=self.root
        for char in word:
            if not cur.children.get(char):
                cur.children[char] = TrieNode(char)
            cur = cur.children[char]
        cur.end = True
        

    def search(self, word):
        cur=self.root
        self.found = False
        self.dfs(cur, word)
        return self.found


    def dfs(self, root, word):
        if not word:
            if root.end:
                self.found = True ###we cant do self.found = root.end caus another dfs might be running
            return
        if word[0] == ".":
            for node in root.children.values():
                self.dfs(node, word[1:])
        else:
            node = root.children.get(word[0])
            if node:
                self.dfs(node, word[1:])
            else:
                return
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
