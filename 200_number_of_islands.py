class Solution(object):
    def p(self, grid):
        for i in range(0,len(grid)):
            print(grid[i])
            

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count=0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j]=="1":
                    self.dfs_rec(i, j, grid)
                    # self.dfs(grid, i, j)
                    count+=1
        return count
    
    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
    
    def dfs_rec(self, i, j, grid):
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]!='1':
            return 
        grid[i][j] = '0'
        self.dfs_rec(i+1, j, grid)
        self.dfs_rec(i-1, j, grid)
        self.dfs_rec(i, j+1, grid)
        self.dfs_rec(i, j-1, grid)
    
    
    def dfs_island(self, x, y, grid, visited):
        mrow, ncol=len(grid), len(grid[0])
        stack=[]
        stack.append([x,y])
        while(len(stack)!=0):
            i,j=stack.pop()

            visited[i][j]=True
            if self.isExists(i, j-1 ,mrow, ncol):
                if grid[i][j-1]=="1" and visited[i][j-1]==False:
                    stack.append([i,j-1])
                    visited[i][j-1]==True

            if self.isExists(i ,j+1,mrow, ncol):
                if grid[i][j+1]=="1" and visited[i][j+1]==False:

                    stack.append([i,j+1])
                    visited[i][j-1]==True

            if self.isExists(i-1,j,mrow, ncol):
                if grid[i-1][j]=="1" and visited[i-1][j]==False:
                    stack.append([i-1,j])
                    visited[i][j-1]==True

            if self.isExists(i+1,j,mrow, ncol):
                if grid[i+1][j]=="1" and visited[i+1][j]==False:
                    stack.append([i+1,j])
                    visited[i][j-1]==True


    def isExists(self, i, j, m, n):
        if i>=m or j>=n or i<0 or j<0:
            return False
        else:
            return True
