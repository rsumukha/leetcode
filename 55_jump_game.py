class Solution(object):
	def canJump(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		#bottomup table
		# return self.bottomup(nums)
		return self.backtracking(nums, 0)



	def bottomup(self, nums):
		dp_array = [0 for i in range(len(nums)+1)]
		for i in range(len(nums)-1):
			dp_array[i+1] = max(dp_array[i], nums[i]+i)
			if dp_array[i+1]==0 or dp_array[i+1]==i:
				return False
		print(dp_array)
		if dp_array[len(nums)-1]>=len(nums)-1:
			return True
		else:
			return False

	def backtracking(self, nums, current):
		if current==len(nums):
			return True
		if nums[current]==0 or nums[current]==current:
			return False
		flag=False
		for i in range(current, len(nums)):
			flag= self.backtracking(nums, nums[i])

		return flag




		


if __name__=="__main__":
	s=Solution()
	print(s.canJump([3,2,1,1,4]))