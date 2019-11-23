class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix)==0:
            return False
        nrow = len(matrix)
        ncol = len(matrix[0])
        
        if nrow == 0 and ncol == 0:
            return False
        i =0
        j =ncol-1
        
        while i<nrow and j>=0:
            if matrix[i][j] == target:
                return True
            elif target > matrix[i][j]:
                i+=1
            else:
                j-=1
        return False
        
        
        
