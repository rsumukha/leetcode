class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_local =nums[0]
        min_ptr=nums[0]
        max_global=nums[0]
        for num in nums[1:]:
            max_local = max(max_local*num, min_ptr*num)
            max_local=max(num, max_local)
            max_global=max(max_global, max_local)
            min_ptr=min(num, min_ptr*num)
        return max_global