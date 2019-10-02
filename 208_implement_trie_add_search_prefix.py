class TrieNode(object):
    def __init__(self, char):
        self.val = char
        self.children = collections.defaultdict(int)
        self.count = 0
        self.end = False


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode("root")

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        currentnode = self.root
        for character in word:
            if currentnode.children[character]==0:
                currentnode.children[character] = TrieNode(character)
            currentnode = currentnode.children[character]
        currentnode.end = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        currentnode = self.root
        for character in word:
            if currentnode.children[character]!=0:
                currentnode = currentnode.children[character]
            else:
                return False
        return currentnode.end
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        currentnode = self.root
        for character in prefix:
            if currentnode.children[character]!=0:
                currentnode = currentnode.children[character]
            else:
                return False
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
