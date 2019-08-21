class TrieNode(object):    
    def __init__(self, char):
        self.char=char
        self.children=[]
        self.end=False

class Solution(object):
    def add(self, word, root):
        node=root        
        for char in word:
            found=False            
            for tnode in node.children:
                if tnode.char==char:
                    found=True
                    node =tnode
                    break;
            if found==False:
                newnode=TrieNode(char)
                node.children.append(newnode)
                node=newnode
        node.end=True
        
    def printall(self, node, level):
        print(node.char+" ")
        if node.end==True:
            return
        for tnode in node.children:
            self.printall(tnode, level+1)        
                                    
    
    def ladderLength(self, beginWord, endWord, wordList):
        root=TrieNode("*")
        for word in wordList:
            self.add(word, root)
        #self.printall(root, 1)
        visited=[]
        visited.append(beginWord)
        length=0
        tobevisited=visited

        while len(tobevisited):
            length+=1
            tnode=root
            cur=tobevisited.pop()
            if cur==endWord:
                return length
            # print(len(cur))
            for ptr in range(len(cur)):
                tnode = self.traverse(ptr, cur, tnode)
                print(ptr, tnode.char)
                if tnode:
                    for node in tnode.children:
                        new_word=cur.replace(cur[ptr], node.char)
                        if not new_word in visited:
                            print(cur, new_word)
                            if self.traverse(len(cur), word[ptr:], tnode):
                                tobevisited.append(new_word)
                                visited.append(new_word)
                                print(tobevisited)
        return 0

    # def word_present(self, word, root):
    #     print("checking if "+word+" present in TREE.")
    #     for i in range(len(word)):
    #         found=False
    #         for node in root.children:



    def traverse(self, p, word, root):
        if p==0:
            return root
        for i in range(0,p):
            found=False
            for node in root.children:
                if node.char==word[i]:
                    root=node
                    found=True
                    break
        if found:
            return root
        else:
            return None




    #     while len(tobevisited):
    #         length+=1
    #         troot=root
    #         current=tobevisited.pop()
    #         self.bfs_narytree(troot, visited, current)

    # def bfs_narytree(self, root, visited, current):
    #     for ptr in range(len(current), 0):
    #         char=current[ptr]
    #         for node in root.children:
    #             if node.char!=char:
    #                 look_bfs(node, )




if __name__=="__main__":
    s=Solution()
    wordList = ["hot","dot","dog","lot","log","cog"]
    print("\nlength "+str(s.ladderLength("hit", "cog", wordList)))
