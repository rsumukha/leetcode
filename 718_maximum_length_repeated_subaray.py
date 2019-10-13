class Solution(object):
    def findLength(self, A, B):
        #same as longest common substring
        # dp with matrix
        if len(A) == 0 or len(B) == 0:
            return 0
        
        dp_array = [[0 for _ in range(len(A)+1)] for _ in range(len(B)+1)]
        maxlength = 0
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    dp_array[i+1][j+1] = dp_array[i][j] + 1
                    maxlength = max(maxlength, dp_array[i+1][j+1])
        return maxlength
        
