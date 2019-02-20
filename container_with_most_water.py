class Solution(object):
    def maxArea(self, height):
        """ #NAIVE SOLUTION
        max = 0
        for i in range(len(height)):
            for j in range(i, len(height)):
                cost = (j - i) * (height[i] if height[i] <= height[j] else height[j])
                if cost > max:
                    max = cost
        return max
        """
        max_area=0
        i=0
        j=len(height)-1
        while(i!=j):
            cost = (j - i) * (height[i] if height[i] <= height[j] else height[j])
            if cost>max_area:
                max_area=cost
            if height[i]>=height[j]:
                j-=1
            else:
                i+=1
        return max_area







if __name__=="__main__":
    s=Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))
