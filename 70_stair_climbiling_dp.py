class Solution:
    def climbStairs(self, n):
        dp_array=[]
        dp_array.append(0)
        dp_array.append(1)
        dp_array.append(2)
        # print(dp_array)
        # return

        if n<=2:
            return dp_array[n]

        for i in range(3,n+1):
            # print(i)
            dp_array.append(dp_array[i-1]+dp_array[i-2])

        return dp_array[n]






if __name__=="__main__":
    s=Solution()
    print(s.climbStairs(4))
    #idea is to store the values as and when you compute so keep an array
    #to climb the stairs 
    #array in c++ has random access so O(1)
    #in python dynamic array so pop front takes O(n) so use dequr