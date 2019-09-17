                
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]

        ->->->->x
                       

        """

        if len(matrix)==0:
            return None
        
        row=len(matrix)
        col=len(matrix[0])
        
        total=row*col
        output_list=[]
        
        i, new_i=0, 0
        j, new_j=0, 0
        
        r=[0, 1, 0, -1]
        c=[1, 0, -1, 0]
        
        seek=0
        while total!=0:
            
            output_list.append(matrix[i][j])
            matrix[i][j]=None
            
            new_i=i+r[seek]
            new_j=j+c[seek]
            
            # print("new_i, new_j")
            # print(new_i, new_j)
            
            if seek==0:
                if new_j>=col:
                    seek=(seek+1)%4
                elif matrix[new_i][new_j]==None:
                    seek=(seek+1)%4
                
            elif seek==1:
                if new_i>=row:
                    seek=(seek+1)%4
                elif matrix[new_i][new_j]==None:
                    seek=(seek+1)%4
        
            elif seek==2:
                if new_j<0:
                    seek=(seek+1)%4
                elif matrix[new_i][new_j]==None:
                    seek=(seek+1)%4
                
            elif seek==3:
                if matrix[new_i][new_j]==None:
                    seek=(seek+1)%4
            
            i+=r[seek]
            j+=c[seek]   
            # print("i,j")
            # print(i,j)
            total-=1
        
        return output_list
            
        
        
                