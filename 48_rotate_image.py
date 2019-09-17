from math import floor
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        #transpose and interchange
        
        n=len(matrix)
        
        for i in range(n):
            for j in range(i+1,n):
                tmp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=tmp
        
        first=0
        last=n-1
        while first<last: #to get to middle always use f<l
            
            for x in range(n):
                tmp=matrix[x][first]
                matrix[x][first] =matrix[x][last]
                matrix[x][last]=tmp
            
            first+=1
            last-=1
            
            
                
        
        