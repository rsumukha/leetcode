class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        eq=0
        for i in nums:
            eq=eq^i
        return eq
        
