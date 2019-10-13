class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #levenshtein distance, DP problem        
        # min [costforinstert + costfordelete + costforreplace]
        self.memo ,i, j = {}, 0,0
        return self.topdownapproach(word1, word2, i, j)
        # self.bottomupapproach(word1, word2)
        # self.backtrack(word1, word2)
    
    def topdownapproach(self, word1, word2, i, j):
        if i==len(word1) and j==len(word2):
            return 0
        if i==len(word1):
            return len(word2) -j
        if j==len(word2):
            return len(word1) -i
        if (i,j) not in self.memo:
            if word1[i] == word2[j]:
                self.memo[(i,j)] = self.topdownapproach(word1, word2, i+1, j+1)
            else:
                insert = 1 + self.topdownapproach(word1, word2, i, j+1)#adding a char to word1 is equal to deleting a char in word2
                delete = 1 + self.topdownapproach(word1, word2, i+1, j)
                replace = 1 + self.topdownapproach(word1, word2, i+1, j+1)
                self.memo[(i,j)] = min(insert, delete, replace)
        
        return self.memo[(i,j)]
    
    def backtrack(word1, word2):
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        if word1[0] == word2[0]:
            return self.backtrack(word1[1:], word2[1:])
        insert = 1 + self.backtrack(word1, word2[1:])
        delete = 1 + self.backtrack(word1[1:], word2)
        replace = 1 + self.backtrack(word1[1:], word[1:])
        return min(insert, delete, replace)
        
    def bottomupapproach(word1, word2):
        #   |replace | insert |
        #   |delete  |  myptr |
        
        dp_array = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        x=0
        for i in range(len(word1)+1):
            dp_array[i][0] = x
            x+=1
        x=0
        for i in range(len(word2)+1):
            dp_array[0][i] = x
            x+=1
        # print(dp_array)
        for i in range(0, len(word1)):
            for j in range(0, len(word2)):
                if word1[i] == word2[j]:
                    dp_array[i+1][j+1] = dp_array[i][j]
                else:
                    dp_array[i+1][j+1] = min( dp_array[i][j+1], dp_array[i+1][j], dp_array[i][j] )+1
        return dp_array[len(word1)][len(word2)]
            
        
        
