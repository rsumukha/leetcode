from copy import deepcopy
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(board)==0:
            return None        
        if len(word)==0:
            return True        
        row=len(board)
        col=len(board[0])        
        found=False
        for i in range(row):
            for j in range(col):
                if board[i][j]==word[0]:
                    found=self.dfs(i, j, board, word, 0)
                    if found:
                        return True
        return found
                    
            
    def dfs(self, i, j, board, word, ptr):
        if len(word)==ptr:
            return True
        if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j]!=word[ptr]:
            return False        
        tmp=board[i][j]
        board[i][j] = '*'
        result = self.dfs(i+1, j, board, word, ptr+1) or self.dfs(i, j+1, board, word, ptr+1) or self.dfs(i-1, j, board, word, ptr+1) or self.dfs(i, j-1, board, word, ptr+1)
        board[i][j]=tmp
        return result
    
    def dfs(self, i, j, board, word, nrow, ncol):
        r=[0,1,0,-1]
        c=[1,0,-1,0]
        
        stack=[]
        v = [[False for _ in range(ncol)] for __ in range(nrow)]
        ptr=0
        stack.append(( [i,j] , ptr, deepcopy(v)))
        
        while len(stack)!=0:
            
            cor, ptr, visited = stack.pop()
            x, y =cor
            ptr+=1            
            if ptr>=len(word):
                break
                
            visited[x][y]=True

            for seek in range(4):
                new_i=x+r[seek]
                new_j=y+c[seek]                
                if new_i>=nrow or new_i<0 or new_j>=ncol or new_j<0:
                    continue
                else:
                    if visited[new_i][new_j]!=True and board[new_i][new_j]==word[ptr]:
                        stack.append( ([new_i,new_j], ptr, deepcopy(visited)) )                        
                        
        if ptr==len(word):
            return True
        else:
            return False