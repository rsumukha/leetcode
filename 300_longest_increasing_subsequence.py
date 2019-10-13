class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0

        dp_array=[1]*(len(nums)+1)

        for i in range(1, len(nums)):
            # print(dp_array)
            for j in range(0, i+1):
                if nums[j]<nums[i]:
                    dp_array[i]=max(dp_array[j]+1, dp_array[i])   # max because there might be a sequence that
                                                                  # 123 15 5678 [10] here it shouldnt take 123
        return max(dp_array)

        

        
        


