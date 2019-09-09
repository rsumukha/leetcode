class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        return self.combinationRecBacktracking(nums, target)
        dp_array=[-1 for i in range(target+1)]
        dp_array[0]=1
        print(dp_array)
        return self.combinationRecDP(nums, target, dp_array)

    def combinationRecBacktracking(self, nums, target):
    	print(nums, target)
    	if target==0:
    		return 1

    	res=0
    	for i in range(len(nums)):
    		if target-nums[i]>=0:
    		    res+=self.combinationRecBacktracking(nums, target-nums[i])
    		    print("res--"+str(res))

    	return res

    def combinationRecDP(self, nums, target, dp_array):
    	if dp_array[target]!= -1:
    		return dp_array[target]

    	result=0
    	for i in range(len(nums)):
    		if target-nums[i]>=0:
    			result+=self.combinationRecDP(nums, target-nums[i], dp_array)
    	dp_array[target]=result

    	return dp_array[target]

      



if __name__=="__main__":
	s=Solution()
	print(s.combinationSum4([1, 2, 3], 4))