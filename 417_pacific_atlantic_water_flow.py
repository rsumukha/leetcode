class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        #Pacific ocean if i<0 or j<0
        #atlantic ocean if i>row or i>col
        if len(matrix) == 0:
            return []
        ans=set()
        if len(matrix) ==1:
            for i in range(len(matrix[0])):
                ans.add((0, i))
        if len(matrix[0]) ==1:
            for i in range(len(matrix)):
                ans.add((i, 0))
        row, col = len(matrix), len(matrix[0])
        canflowpacific = [[False for _ in range(col)] for _ in range(row)]
        canflowatlantic = [[False for _ in range(col)] for _ in range(row)]
        
        def dfs(i, j, visited):
            visited[i][j] =True
            for x,y in [(1,0), (0,1), (-1,0), (0,-1)]:
                x, y =i+x, j+y
                if x<0 or y<0 or x>=row or y>=col or visited[x][y] or matrix[x][y] < matrix[i][j]:
                    continue
                dfs(x, y, visited)                        
                        
        for i in range(row):
            dfs(i, 0, canflowpacific)
            dfs(i, col-1, canflowatlantic)
        for j in range(col):
            dfs(0, j, canflowpacific)
            dfs(row-1, j, canflowatlantic)
        for i in range(row):
            for j in range(col):
                    if canflowpacific[i][j] and canflowatlantic[i][j]:
                        ans.add((i, j))
        return list(ans)
        
        
