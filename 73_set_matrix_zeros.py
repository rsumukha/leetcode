class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """    
        #using extra space
        row=len(matrix)
        col=len(matrix[0])
        
        row_set=set()
        col_set=set()
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    row_set.add(i)
                    col_set.add(j)
                    
        for ro in row_set:
            for _ in range(col):
                matrix[ro][_]=0
        
        for co in col_set:
            for _ in range(row):
                matrix[_][co]=0
                    
                    
                    
                    
                    