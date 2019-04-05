class Solution(object):
    def p(self, grid):
        for i in range(0,len(grid)):
            print(grid[i])
            

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # print(len(grid[0]))
        self.p(grid)
        count=0
        visited=[[False for i in range(0,len(grid[0]))] for j in range(0, len(grid))]
        # print(visited)
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                # print(visited[i][j])
                # print(grid[i][j])
                if visited[i][j]==False and grid[i][j]=="1":
                    self.dfs_island(i, j, grid, visited)
                    count+=1
        return count
    
    def dfs_island(self, x, y, grid, visited):
        # print("here")
        mrow, ncol=len(grid), len(grid[0])
        print(mrow, ncol)
        stack=[]
        stack.append([x,y])
        while(len(stack)!=0):
            # print(stack)
            i,j=stack.pop()

            visited[i][j]=True
            if self.isExists(i, j-1 ,mrow, ncol):
                if grid[i][j-1]=="1" and visited[i][j-1]==False:
                    stack.append([i,j-1])

            if self.isExists(i ,j+1,mrow, ncol):
                if grid[i][j+1]=="1" and visited[i][j+1]==False:

                    stack.append([i,j+1])

            if self.isExists(i-1,j,mrow, ncol):
                if grid[i-1][j]=="1" and visited[i-1][j]==False:
                    stack.append([i-1,j])

            if self.isExists(i+1,j,mrow, ncol):
                print(i,j)
                if grid[i+1][j]=="1" and visited[i+1][j]==False:
                    stack.append([i+1,j])

            # if self.isExists(i+1,j-1,mrow, ncol):
            #     if grid[i+1][j-1]=="1" and visited[i+1][j-1]==False:
            #         stack.append([i+1,j-1])

            # if self.isExists(i+1,j+1,mrow, ncol):
            #     if grid[i+1][j+1]=="1" and visited[i+1][j+1]==False:
            #         stack.append([i+1,j+1])

            # if self.isExists(i-1,j-1,mrow, ncol):
            #     if grid[i-1][j-1]=="1" and visited[i-1][j-1]==False:
            #         stack.append([i-1,j-1])

            # if self.isExists(i-1,j+1,mrow, ncol):
            #     if grid[i-1][j+1]=="1" and visited[i-1][j+1]==False:
            #         stack.append([i-1,j+1])

    def isExists(self, i, j, m, n):
        if i>=m or j>=n or i<0 or j<0:
            return False
        else:
            return True



if __name__=="__main__":
    s=Solution()
    print(s.numIslands(  [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]  ))

        
        
        