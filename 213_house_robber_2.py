class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return nums[0]
            else:
                return nums[1]
        return max(self.oldRob(nums[0:len(nums)-1]), self.oldRob(nums[1:len(nums)]))
        
        
    def oldRob(self, nums):
        print(nums)
        ptrEven=nums[0]
        ptrOdd=nums[1]
        for i in range(2, len(nums)):
            odd=i%2
            
            if odd:
                ptrEven=max(ptrEven, ptrOdd)
                ptrOdd+=nums[i]
                
            else:
                ptrOdd=max(ptrEven, ptrOdd)
                ptrEven+=nums[i]
                
        print(ptrOdd, ptrEven)
        return max (ptrOdd, ptrEven)
        
        