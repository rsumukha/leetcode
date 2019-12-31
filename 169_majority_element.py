class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxele = None
        curcnt = 0
        countdict = {}
        for num in nums:
            if num in countdict:
                countdict[num] += 1
            else:
                countdict[num] = 1
            
            if countdict[num] > curcnt:
                curcnt = countdict[num]
                maxele = num
        return maxele
        
