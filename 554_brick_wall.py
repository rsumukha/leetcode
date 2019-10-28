class Solution(object):
    def leastBricks(self, wall):
        dictionary = {}
        
        numberpfspaces = 0
        for row in wall:
            numberofspaces = 0
            for eachbrick in row[:len(row)-1]:
                numberofspaces += eachbrick
                if numberofspaces in dictionary:
                    dictionary[numberofspaces] += 1
                else:
                    dictionary[numberofspaces] = 1
        # print(dictionary)
        return len(wall) - max(dictionary.values() if len(dictionary.values())!=0 else [0])
        
        
        
        
        
        
        # bruteforce, takes too much space
        total = sum(wall[0])
        if total == 1:
            return len(wall)
        
        brickmatrix = [[0 for _ in range(total)] for _ in range(len(wall))]
        
        def buildwall(row, w):
            col = 0
            bricknumber = 1
            for numberofbricks in w:
                n = numberofbricks
                while n:
                    brickmatrix[row][col] = bricknumber
                    n -= 1
                    col += 1
                bricknumber +=1
        
        for i,eachwall in enumerate(wall):
            buildwall(i, eachwall)
        
        print(brickmatrix)
        
        minimumbricks = float("inf")
        for j in range(len(brickmatrix[0])-1):
            localmin = 0
            for i in range(len(brickmatrix)):
                if brickmatrix[i][j] == brickmatrix[i][j+1]:
                    localmin += 1
                    
            minimumbricks = min(minimumbricks, localmin)
        return minimumbricks
    
    
        
        
