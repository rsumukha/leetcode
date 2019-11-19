"""
TP: combinatorics problem can be solved using dp
1 -> 1
2 -> 2
3-> 1 and 2 as right     
    2 and 1 as left
    
use this to calculate n = 4



1, 2, 3, 4, 5:
1 as root and (2,3,4,5)
2 as root 1 as left and (3,4,5) as right
3 as root (1,2) as left and (4,5) as right
4 as root (1,2,3) as left and (5) as right
5 as root (1,2,3,4) as left
"""

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        
        dp_array = [0 for i in range(n+1)]
        dp_array[1] = 1
        
        for i in range(2, n+1):
            for j in range(1,i+1):
                if dp_array[j-1] == 0:
                    dp_array[i] += dp_array[i-j]
                elif dp_array[i-j] == 0:
                    dp_array[i] += dp_array[j-1]
                else:
                    dp_array[i] +=  dp_array[i-j] * dp_array[j-1]
                # print(i, j, dp_array)

            
        return dp_array[-1]
        
