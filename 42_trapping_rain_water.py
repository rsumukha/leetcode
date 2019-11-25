"""
TP: total water is min(longest building to the right , THe longest building to the left) - current_height
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        if len(height) == 0:
            return 0
        
        leftarray = [0 for i in range(len(height)+1)]
        rightarray = [0 for i in range(len(height)+1)]
        leftarray[0] = height[0]
        rightarray[len(height)-1] = height[len(height)-1]
        total = 0
        
        for i in range(1, len(height)):
            leftarray[i] = max(leftarray[i-1], height[i])
        for i in range(len(height)-1, -1, -1):
            rightarray[i] = max(rightarray[i+1], height[i])
            total += (min(leftarray[i], rightarray[i]) - height[i])
            
        return total
            
        
