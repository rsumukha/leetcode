class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers)==0:
            return None
        
        leftptr=0
        rightptr=len(numbers)-1
        output=[]
        while leftptr<rightptr:
            if numbers[rightptr]+numbers[leftptr]>target:
                rightptr-=1
            elif numbers[rightptr]+numbers[leftptr]<target:
                leftptr+=1
            else:
                output.append(leftptr+1)
                output.append(rightptr+1)
                return output
        
        return output