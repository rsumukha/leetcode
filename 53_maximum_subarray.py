class Solution(object):
    def maxSubArray(self, nums):
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        
        start, end =0,1
        maxtotal = nums[0]
        total = maxtotal
        for end in range(1, len(nums)):
            total = max(nums[end], total+nums[end])
            maxtotal = max (maxtotal, total)
        return maxtotal
        
        
