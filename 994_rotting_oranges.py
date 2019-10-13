class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        #BFS implementation
        # at t = n , all nth level orange will be rotten so it is level order traversal, so BFS
        # do it till we find no more oranges to rot
        #
        
        if len(grid) == 0 and len(grid[0]) == 0:
            return 0
        row, col = len(grid), len(grid[0])
        freshorangecount, totaltime = 0, 0
        queue = collections.deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    freshorangecount +=1
                if grid[i][j] == 2:
                    queue.append((i,j))
        queue.append(None)
                    
        while queue:
            # print(queue)
            cur = queue.popleft()
            if cur:
                x,y = cur
                for i, j in [(0,1), (1,0), (-1,0), (0,-1)]:
                    i, j = x+i, y+j
                    if i<0 or i>=row or j<0 or j>=col:
                        continue
                    if grid[i][j] == 1:
                        queue.append((i,j))
                        grid[i][j] = 2
                        freshorangecount -=1
            else:
                if len(queue):
                    queue.append(None)
                    totaltime +=1
        return -1 if freshorangecount!=0 else totaltime 
                
                
