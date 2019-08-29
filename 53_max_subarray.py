class Solution:
    def maxSubArray(self, nums):
    	max_local=nums[0]
    	max_global=nums[0]
    	for i in range(len(nums)):
    		max_local=max(max_local+nums[i], nums[i])
    		max_global=max(max_global, max_local)
    	return max_global


if __name__=="__main__":
 	s=Solution()
 	print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
        