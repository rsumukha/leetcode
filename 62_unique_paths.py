class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # print(dp_array)
        # exit(0)
        return self.bottomup(m, n)
        return self.topdown(m, n, 0,0 , dp_array)
        return self.recursion(m, n, 1,1)

    #bottomup table
    def bottomup(self, m, n):
    	dp_array=[[0 for i in range(n+1)] for i in range(m+1)]


    	dp_array[0][1]=1
    	for i in range(m):
    		for j in range(n):
    			dp_array[i+1][j+1]=dp_array[i+1][j]+dp_array[i][j+1]
    	# print(dp_array)
    	return dp_array[m][n]


    #recursiove topdown
    def topdown(self, m, n, i, j, dp_array):
    	if m==i+1 and n==j+1:
    		return 1
    	if dp_array[i][j]!=0:
    		return dp_array[i][j]

    	total=0
    	if i+1<m:
    		total+=self.topdown(m, n, i+1, j, dp_array)
    	if j+1<n:
    		total+=self.topdown(m, n, i, j+1, dp_array)
    	dp_array[i][j]= total

    	return dp_array[i][j]


    #recursive solution
    def recursion(self, m, n, i, j):
        if i==m and j==n:
            return 1
        
        total=0
        if i+1<=m:
            total+=self.recursion(m, n, i+1, j)
        if j+1<=n:
            total+=self.recursion(m, n, i, j+1)
        return total
        

if __name__=="__main__":
	s=Solution()
	print(s.uniquePaths(3,2))